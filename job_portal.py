import feedparser
from datetime import datetime, timedelta

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
                published = entry.get('published', 'N/A')
                category = entry.get('category', 'N/A')

                published_date = datetime.strptime(published, "%a, %d %b %Y %H:%M:%S %Z")

                job = JobListing(title, company, location, job_type, link, published, category)
                self.job_listings.append(job)
        else:
            print("No entries found in the RSS feed.")

    def get_recent_job_listings(self, days=1):
        now = datetime.utcnow()
        recent_listings = [
            job for job in self.job_listings if job.published >= now - timedelta(days=days)
        ]
        return recent_listings