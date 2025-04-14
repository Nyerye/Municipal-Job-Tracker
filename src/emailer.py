# src/emailer.py

import yagmail
import os
from dotenv import load_dotenv

load_dotenv()  # Load credentials from .env

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# Function for controlling the email being sent
def send_email(jobs):

    # IF you are getting errors in the terminal, you MUST add in your credentials to the .env file and you need to make a Google App Password. See the README for more details.
    if not (SENDER_EMAIL and SENDER_PASSWORD and RECIPIENT_EMAIL):
        print("[ERROR] Missing email config in .env")
        return

    if not jobs:
        print("[INFO] No jobs to send.")
        return

    subject = "New IT Job Postings Found"
    body_lines = ["Here are the new job postings:\n"]

    for job in jobs:
        line = f"{job['city']} - {job['title']}\n{job['url']}\n"
        body_lines.append(line)

    body = "\n".join(body_lines)

    try:
        yag = yagmail.SMTP(SENDER_EMAIL, SENDER_PASSWORD)
        yag.send(to=RECIPIENT_EMAIL, subject=subject, contents=body)
        print("✅ Email sent successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")
