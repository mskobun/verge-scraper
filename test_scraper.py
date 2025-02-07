from verge_scraper.scraper import VergeArchiveScraper
from datetime import datetime


def main():
    # Example usage
    scraper = VergeArchiveScraper()

    try:
        # Configure year and month here
        year = 2022
        month = 2

        articles = scraper.scrape_archive(year, month)

        # Print summary
        print(f"\nTotal articles found: {len(articles)}")

        # Print first few articles as sample
        print("\nSample of first 5 articles:")
        for article in articles[:5]:
            print("\n---Article---")
            print(article)
            if article.date:
                print(
                    f"Formatted Date: {article.date.strftime('%Y-%m-%d %H:%M:%S UTC')}"
                )

        # Print date range
        if articles:
            dates = [a.date for a in articles if a.date]
            if dates:
                print(f"\nDate range: {min(dates)} to {max(dates)}")
                print(
                    f"Articles per day: {len(articles) / len(set(d.date() for d in dates)):.1f}"
                )

    except Exception as e:
        print(f"Error: {e}")


def print_article(article):
    """Test specific properties of an article"""
    print("\nDetailed Article Test:")
    print(f"Title length: {len(article.title)}")
    print(f"URL valid: {article.url.startswith('http')}")
    print(f"Number of authors: {len(article.authors.split(','))}")
    if article.date:
        print(f"Is recent: {article.date > datetime(2024, 1, 1)}")


if __name__ == "__main__":
    main()
