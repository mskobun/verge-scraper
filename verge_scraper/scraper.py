import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
from datetime import datetime
import logging
import json
from dataclasses import dataclass
import time


@dataclass
class Article:
    """Represents an article from The Verge"""

    title: str
    url: str
    authors: str
    date: Optional[datetime]

    @classmethod
    def from_json(cls, data: Dict) -> "Article":
        """Create an Article instance from JSON data"""
        # Process authors
        authors = ""
        for author in data.get("authors", []):
            authors += author.get("name", "") + ", "
        # Remove the last comma and space
        authors = authors[:-2] if authors else "Unknown Author"

        # Process date
        published_date = None
        if data.get("publishedAt"):
            try:
                published_date = datetime.fromisoformat(
                    data["publishedAt"].replace("Z", "+00:00")
                )
            except ValueError:
                logging.error(f"Error parsing date: {data['publishedAt']}")

        return cls(
            title=data.get("title", ""),
            url=data.get("permalink", ""),
            authors=authors,
            date=published_date,
        )

    def __str__(self) -> str:
        """String representation of the article"""
        return (
            f"Title: {self.title}\n"
            f"URL: {self.url}\n"
            f"Authors: {self.authors}\n"
            f"Date: {self.date}\n"
        )


class VergeArchiveScraper:
    def __init__(self, request_delay: float = 1.0):
        self.base_url = "https://www.theverge.com/archives"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        self.request_delay = request_delay
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def get_archive_page(self, year: int, month: int) -> str:
        """
        Construct and return the archive URL for a specific year and month
        """
        return f"{self.base_url}/{year}/{month}"

    def fetch_page(self, url: str) -> BeautifulSoup:
        """
        Fetch the page content and return BeautifulSoup object
        """
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return BeautifulSoup(response.text, "html.parser")
        except requests.RequestException as e:
            self.logger.error(f"Error fetching page: {e}")
            raise

    def parse_articles(
        self, soup: BeautifulSoup
    ) -> tuple[List[Article], Optional[int]]:
        """
        Parse articles from the archive page
        Returns tuple of (articles, total_pages)
        """
        articles = []
        total_pages = None

        script_tag = soup.find("script", {"id": "__NEXT_DATA__"})
        if not script_tag:
            self.logger.warning("Could not find __NEXT_DATA__ script tag")
            return articles, total_pages

        try:
            data = json.loads(script_tag.string)
            entries = (
                data.get("props", {})
                .get("pageProps", {})
                .get("hydration", {})
                .get("responses", [])
            )

            if not entries:
                return articles, total_pages

            # Find the archive data in responses
            for entry in entries:
                if entry.get("operationName") == "FullArchiveLayoutQuery":
                    archive_data = (
                        entry.get("data", {}).get("resource", {}).get("posts", {})
                    )

                    # Get total pages from pageInfo
                    page_info = archive_data.get("pageInfo", {})
                    total_pages = page_info.get("totalPages", 0)

                    # Get articles from nodes
                    nodes = archive_data.get("nodes", [])
                    for article_data in nodes:
                        try:
                            article = Article.from_json(article_data)
                            articles.append(article)
                        except Exception as e:
                            self.logger.error(f"Error parsing article data: {e}")
                    break

        except json.JSONDecodeError as e:
            self.logger.error(f"Error decoding JSON data: {e}")
        except Exception as e:
            self.logger.error(f"Error parsing articles: {e}")

        return articles, total_pages

    def scrape_archive_page(self, year: int, month: int, page: int) -> List[Article]:
        """
        Scrape a specific page of articles from the archive
        """
        try:
            current_year = datetime.now().year
            if not (2011 <= year <= current_year and 1 <= month <= 12):
                raise ValueError(f"Invalid year/month combination: {year}/{month}")

            url = f"{self.get_archive_page(year, month)}/{page}"
            self.logger.info(f"Fetching page {page}: {url}")

            soup = self.fetch_page(url)
            articles, total_pages = self.parse_articles(soup)

            if not articles:
                self.logger.warning(f"No articles found on page {page}")
            else:
                self.logger.info(f"Found {len(articles)} articles on page {page}")

            return articles

        except Exception as e:
            self.logger.error(f"Error scraping page {page}: {e}")
            raise

    def scrape_archive(self, year: int, month: int) -> List[Article]:
        """
        Main method to scrape all articles from a specific year and month
        This is now implemented using scrape_archive_page
        """
        try:
            current_year = datetime.now().year
            if not (2011 <= year <= current_year and 1 <= month <= 12):
                raise ValueError(f"Invalid year/month combination: {year}/{month}")

            # Get first page and total page count
            articles = self.scrape_archive_page(year, month, 1)
            _, total_pages = self.parse_articles(
                self.fetch_page(f"{self.get_archive_page(year, month)}/1")
            )

            if not total_pages:
                self.logger.warning("Could not determine total pages")
                return articles

            self.logger.info(f"Found {total_pages} total pages")

            # Get remaining pages
            for page in range(2, total_pages + 1):
                page_articles = self.scrape_archive_page(year, month, page)
                articles.extend(page_articles)
                time.sleep(self.request_delay)

            self.logger.info(
                f"Successfully scraped {len(articles)} articles from {total_pages} pages"
            )
            return articles

        except Exception as e:
            self.logger.error(f"Error scraping archive: {e}")
            raise

    def test_scrape(self):
        """
        Test method to verify scraper functionality
        """
        try:
            year = 2025
            month = 1
            articles = self.scrape_archive(year, month)

            if not articles:
                self.logger.warning("No articles found!")
                # Print the HTML content for debugging
                url = self.get_archive_page(year, month)
                soup = self.fetch_page(url)
                self.logger.debug(f"Raw HTML content: {soup.prettify()}")
            else:
                self.logger.info(f"Found {len(articles)} articles")
                # Print first article for verification
                if articles:
                    self.logger.info(f"Sample article: {articles[0]}")

            return articles

        except Exception as e:
            self.logger.error(f"Test scrape failed: {e}")
            raise
