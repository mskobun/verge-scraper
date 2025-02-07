from flask import Flask, render_template, request
from verge_scraper.scraper import VergeArchiveScraper, Article
from datetime import datetime, timedelta
import calendar
import os
import redis
import json
from typing import List, Dict, Tuple, Optional
from urllib.parse import urlparse

app = Flask(__name__)

# Redis setup with Heroku Redis URL support
redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
# Stupid Heroku workaround https://stackoverflow.com/questions/65042551/ssl-certification-verify-failed-on-heroku-redis
redis_url += "?ssl_cert_reqs=none"
redis_client = redis.from_url(redis_url, decode_responses=True)

REQUEST_DELAY = float(os.getenv("SCRAPER_REQUEST_DELAY", "0.2"))
# 1 hour
CURRENT_MONTH_CACHE_EXPIRY = int(os.getenv("CURRENT_MONTH_CACHE_EXPIRY", str(60 * 60)))


def get_date_range():
    """Get the from_date and to_date from request parameters"""
    today = datetime.now().date()
    min_date = datetime(2022, 1, 1).date()

    try:
        # Get dates from request parameters
        to_date = request.args.get("to_date")
        from_date = request.args.get("from_date")

        if to_date and from_date:
            # Parse the provided dates
            to_date = datetime.fromisoformat(to_date).date()
            from_date = datetime.fromisoformat(from_date).date()
        else:
            # Default to last 7 days if no dates provided
            to_date = today
            from_date = today - timedelta(days=7)

        # Validate dates
        if from_date > to_date:
            from_date, to_date = to_date, from_date

        if from_date < min_date:
            from_date = min_date
        if to_date < min_date:
            to_date = min_date
        if to_date > today:
            to_date = today
        if from_date > today:
            from_date = today

    except (ValueError, TypeError):
        # If invalid dates provided, fallback to default
        to_date = today
        from_date = today - timedelta(days=7)

    return from_date, to_date


def get_page_key(year: int, month: int, page: int) -> str:
    """Generate Redis key for a specific page"""
    return f"verge:page:{year}:{month}:{page}"


def get_page_date_index_key(year: int, month: int) -> str:
    """Generate Redis key for page-to-date index"""
    return f"verge:date_index:{year}:{month}"


def store_page_date_index(year: int, month: int, page: int, dates: List[datetime.date]):
    """Store the mapping of dates to page numbers"""
    index_key = get_page_date_index_key(year, month)
    date_data = {date.isoformat(): page for date in dates}

    # Update or create the index
    existing_data = redis_client.get(index_key)
    if existing_data:
        try:
            existing_index = json.loads(existing_data)
            existing_index.update(date_data)
            redis_client.set(index_key, json.dumps(existing_index))
        except json.JSONDecodeError:
            # If the existing data is corrupt, just set new data
            redis_client.set(index_key, json.dumps(date_data))
    else:
        redis_client.set(index_key, json.dumps(date_data))


def get_pages_for_date_range(
    year: int, month: int, start_date: datetime.date, end_date: datetime.date
) -> List[int]:
    """Get the page numbers needed for a date range"""
    index_key = get_page_date_index_key(year, month)
    date_index = redis_client.get(index_key)

    if not date_index:
        return []  # We'll need to fetch and build the index

    date_index = json.loads(date_index)
    needed_pages = set()

    current = start_date
    while current <= end_date:
        if current.year == year and current.month == month:
            page = date_index.get(current.isoformat())
            if page:
                needed_pages.add(page)
        current += timedelta(days=1)

    return sorted(list(needed_pages))


def get_cached_page(year: int, month: int, page: int) -> List[Article]:
    """Get or fetch a specific page of articles"""
    cache_key = get_page_key(year, month, page)

    # Try to get from Redis cache first
    cached_data = redis_client.get(cache_key)
    if cached_data:
        articles_data = json.loads(cached_data)
        return [
            Article(
                title=art["title"],
                url=art["url"],
                authors=art["authors"],
                date=datetime.fromisoformat(art["date"]) if art["date"] else None,
            )
            for art in articles_data
        ]

    # If not in cache, fetch from scraper
    scraper = VergeArchiveScraper(request_delay=REQUEST_DELAY)
    try:
        articles = scraper.scrape_archive_page(year, month, page)
        valid_articles = [article for article in articles if article.date is not None]

        # Cache the articles
        articles_data = [
            {
                "title": art.title,
                "url": art.url,
                "authors": art.authors,
                "date": art.date.isoformat() if art.date else None,
            }
            for art in valid_articles
        ]

        # Only set expiry for current month
        current_date = datetime.now()
        if year == current_date.year and month == current_date.month:
            redis_client.setex(
                cache_key,
                CURRENT_MONTH_CACHE_EXPIRY,
                json.dumps(articles_data),
            )
        else:
            redis_client.set(cache_key, json.dumps(articles_data))

        return valid_articles
    except Exception as e:
        print(f"Error scraping {year}/{month} page {page}: {e}")
        return []


def get_cached_articles_for_date_range(
    from_date: datetime.date, to_date: datetime.date
) -> List[Article]:
    """Get articles for a date range, fetching pages until we find the dates we need"""
    all_articles = []
    today = datetime.now().date()

    # Don't try to fetch articles from the future
    if from_date > today:
        return []
    if to_date > today:
        to_date = today

    # Group by month
    current = from_date
    while current <= to_date:
        year, month = current.year, current.month
        page = 1
        found_older_date = False

        while not found_older_date:
            articles = get_cached_page(year, month, page)
            if not articles:  # No more articles for this month
                break

            # Check if we've gone past our date range
            oldest_date = min(
                (art.date.date() for art in articles if art.date), default=None
            )

            # Filter articles for the date range
            filtered_articles = [
                article
                for article in articles
                if article.date and from_date <= article.date.date() <= to_date
            ]
            all_articles.extend(filtered_articles)

            if oldest_date and oldest_date < from_date:
                found_older_date = True

            page += 1

        # Move to next month
        if month == 12:
            current = datetime(year + 1, 1, 1).date()
        else:
            current = datetime(year, month + 1, 1).date()

    # Sort all articles by date
    all_articles.sort(key=lambda x: x.date, reverse=True)
    return all_articles


@app.route("/")
def index():
    from_date, to_date = get_date_range()
    articles = get_cached_articles_for_date_range(from_date, to_date)

    # Calculate next/prev date ranges
    date_range = (to_date - from_date).days

    # Calculate next period
    next_from = min(to_date + timedelta(days=1), datetime.now().date())
    next_to = min(next_from + timedelta(days=date_range), datetime.now().date())
    has_next = next_from < datetime.now().date() and next_from < next_to

    # Calculate previous period
    prev_to = from_date - timedelta(days=1)
    prev_from = prev_to - timedelta(days=date_range)
    min_date = datetime(2022, 1, 1).date()
    has_prev = prev_to >= min_date and prev_from < prev_to

    # Adjust prev_from if it would go before 2022
    if prev_from < min_date:
        prev_from = min_date

    return render_template(
        "index.html",
        articles=articles,
        from_date=from_date,
        to_date=to_date,
        has_prev=has_prev,
        has_next=has_next,
        prev_from=prev_from.isoformat() if has_prev else None,
        prev_to=prev_to.isoformat() if has_prev else None,
        next_from=next_from.isoformat() if has_next else None,
        next_to=next_to.isoformat() if has_next else None,
        current_date=f"{from_date.strftime('%B %d, %Y')} - {to_date.strftime('%B %d, %Y')}",
    )


if __name__ == "__main__":
    app.run(debug=True)
