# src/save_jobs.py

import csv
from datetime import datetime
from pathlib import Path
from job_scraper import scrape_jobs  # assumes job_scraper.py is in the same folder

def save_jobs_to_csv(jobs, filepath="data/jobs.csv"):
    Path("data").mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["timestamp", "city", "title", "url"])
        writer.writeheader()
        for job in jobs:
            writer.writerow({
                "timestamp": timestamp,
                "city": job["city"],
                "title": job["title"],
                "url": job["url"]
            })

if __name__ == "__main__":
    jobs = scrape_jobs()
    save_jobs_to_csv(jobs)
    print(f"✅ Saved {len(jobs)} job(s) to data/jobs.csv")
