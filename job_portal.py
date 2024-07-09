import feedparser
from datetime import datetime, timedelta, timezone
import logging
import time

class JobListing:
    def __init__(self, title, company, location, job_type, link, published, category):
        self.title = title
        self.company = company
        self.location = location
        self.job_type = job_type
        self.link = link
        self.published = published
        self.category = category

class JobPortal:
    def __init__(self, feed_url):
        self.feed_url = feed_url
        self.job_listings = []

    def fetch_jobs(self):
        job_feed = feedparser.parse(self.feed_url)
        if job_feed.entries:
            for entry in job_feed.entries:
                title = entry.title
                company = entry.get('company', 'N/A')
                location = entry.get('location', 'N/A')
                job_type = entry.get('type', 'N/A')
                link = entry.link
                published_parsed = entry.get('published_parsed', None)
                category = entry.get('category', 'N/A')

                if published_parsed is None:
                    logging.error("Skipping job entry due to missing published date")
                    continue

                published_date = datetime.fromtimestamp(
                    time.mktime(published_parsed), tz=timezone.utc
                )
                
                job = JobListing(title, company, location, job_type, link, published_date, category)
                self.job_listings.append(job)
        else:
            logging.info("No entries found in the RSS feed.")

    def get_recent_job_listings(self, days=1):
        now = datetime.now(timezone.utc)
        recent_listings = [
            job for job in self.job_listings if job.published >= now - timedelta(days=days)
        ]
        return recent_listings