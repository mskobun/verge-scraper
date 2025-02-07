# The Verge Article Archive

A Flask web application that displays articles from The Verge's archive with date-based navigation.

The application has a 0.2 sec fetching delay to avoid being blocked by the server, which adds up as each month of The Verge archive could get to 60-100 pages. This is somewhat mitigated by Redis caching, but it's not a perfect solution. In addition, currently the logic is to cache individual Verge archive pages in Redis, then fetch them one by one and check if the date is within the requested range. This is efficient if the user only clicks the previous button but obviously not the best solution.

The rationale for chosing The Verge out of the provided websites is somewhat described in <WEBSITES.md>.

## Features
- Browse articles by date range
- Redis caching for improved performance
- Date-based navigation

## Local Development

1. Install dependencies using Poetry:
```bash
poetry install
```

2. Start Redis server:
```bash
redis-server
```

3. Run the app:
```bash
poetry run flask run
```

## Heroku Deployment

1. Install the Heroku CLI and login:
```bash
heroku login
```

2. Create a new Heroku app:
```bash
heroku create your-app-name
```

3. Add Redis add-on:
```bash
heroku addons:create heroku-redis:mini
```

4. Configure environment variables:
```bash
heroku config:set SCRAPER_REQUEST_DELAY=0.2
heroku config:set CURRENT_MONTH_CACHE_EXPIRY=86400
```

5. Deploy to Heroku:
```bash
git add .
git commit -m "Heroku deployment"
git push heroku master
```
6. Open the app:
```bash
heroku open
```

## Environment Variables

- `REDIS_URL`: Full Redis URL (set automatically by Heroku Redis add-on)
- `REDIS_HOST`: Redis server host (fallback if REDIS_URL not set)
- `REDIS_PORT`: Redis server port (fallback if REDIS_URL not set)
- `REDIS_DB`: Redis database number (default: 0)
- `SCRAPER_REQUEST_DELAY`: Delay between scraping requests in seconds (default: 0.2)
- `CURRENT_MONTH_CACHE_EXPIRY`: Cache expiry time for current month in seconds (default: 86400)

## Monitoring

Monitor your app's logs:
```bash
heroku logs --tail
```

Check dyno status:
```bash
heroku ps
```

## Troubleshooting

If you encounter issues:
1. Check the logs: `heroku logs --tail`
2. Verify Redis connection: `heroku redis:info`
3. Restart the app: `heroku restart`
4. Check dyno status: `heroku ps`