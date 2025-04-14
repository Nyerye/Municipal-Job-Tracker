

import requests
from bs4 import BeautifulSoup

KEYWORDS = [
    "IT", "Systems Analyst", "Embedded Developer", "Programmer",
    "Analyst", "System Administrator", "Service Desk"
]

# Job board URLs for each municipality (where available)
CITY_URLS = {
    "City of Guelph": "https://guelph.ca/careers/",
    "City of Cambridge": "https://www.cambridge.ca/en/your-city/current-opportunities.aspx",
    "City of Kitchener": "https://www.kitchener.ca/en/city-services/careers.aspx",
    "City of Waterloo": "https://www.waterloo.ca/en/government/current-opportunities.aspx",
    "City of Toronto": "https://jobs.toronto.ca/jobsatcity/",
    "City of Mississauga": "https://jobs.mississauga.ca/",
    "Norfolk County": "https://www.norfolkcounty.ca/government/employment-opportunities/",
    "City of Hamilton": "https://www.hamilton.ca/jobs-city",
    "City of Brantford": "https://www.brantford.ca/en/living-here/careers.aspx",
    "City of London": "https://careers.london.ca/",
    "Wellington County": "https://www.wellington.ca/en/government/employmentopportunities.aspx",
    "Region of Waterloo": "https://www.regionofwaterloo.ca/en/regional-government/careers.aspx",
    "City of Burlington": "https://www.burlington.ca/en/your-city/careers.asp",
    "Halton Region": "https://www.halton.ca/The-Region/Careers"
}

def keyword_match(text):
    return any(keyword.lower() in text.lower() for keyword in KEYWORDS)

def scrape_city(city, url):
    jobs = []
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "lxml")

        for link in soup.find_all("a"):
            text = link.get_text(strip=True)
            href = link.get("href", "")
            if keyword_match(text):
                full_url = href if href.startswith("http") else f"{url.rstrip('/')}/{href.lstrip('/')}"
                jobs.append({
                    "city": city,
                    "title": text,
                    "url": full_url
                })

    except Exception as e:
        print(f"[ERROR] Could not scrape {city}: {e}")
    return jobs

def scrape_jobs():
    all_jobs = []
    for city, url in CITY_URLS.items():
        print(f"Scraping {city}...")
        city_jobs = scrape_city(city, url)
        all_jobs.extend(city_jobs)
    return all_jobs
