# src/main.py

from job_scraper import scrape_jobs
from emailer import send_email
import logging

def main():
    try:
        logging.basicConfig(level=logging.INFO, filename="logs/tracker.log", filemode="a",
                            format="%(asctime)s - %(levelname)s - %(message)s")

        jobs = scrape_jobs()
        
        if jobs:
            logging.info(f"Found {len(jobs)} job(s). Sending email...")
            send_email(jobs)
        else:
            logging.info("No new jobs found.")

    except Exception as e:
        logging.error(f"Error in main: {e}")

if __name__ == "__main__":
    main()
