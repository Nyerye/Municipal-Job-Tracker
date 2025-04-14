# src/main.py

# Main entry point. Imports cusotm and standard libraries for functions
from job_scraper import scrape_jobs
from emailer import send_email
import logging

def main():
    try:
        logging.basicConfig(level=logging.INFO, filename="logs/tracker.log", filemode="a",
                            format="%(asctime)s - %(levelname)s - %(message)s")

        jobs = scrape_jobs()
        
        # Only if something is found will it print this in the Terminal of choice. 
        if jobs:
            logging.info(f"Found {len(jobs)} job(s). Sending email...")
            send_email(jobs)
        else:
            logging.info("No new jobs found.")

    except Exception as e:
        logging.error(f"Error in main: {e}")

if __name__ == "__main__":
    main()
