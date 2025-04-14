

import requests
from bs4 import BeautifulSoup
import re

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

job_titles = [
    "IT Support Specialist", "IT Support Technician", "Service Desk Analyst", "Help Desk Analyst",
    "Desktop Support Technician", "Technical Support Specialist", "End User Support Technician",
    "IT Operations Analyst", "Systems Analyst", "Business Systems Analyst", "IT Analyst",
    "Network Analyst", "Network Administrator", "Network Engineer", "Infrastructure Analyst",
    "Infrastructure Specialist", "System Administrator", "Linux Administrator", "Windows Administrator",
    "Cloud Administrator", "Cloud Engineer", "Cloud Solutions Architect", "Cybersecurity Analyst",
    "Security Analyst", "Information Security Analyst", "Security Engineer", "Security Administrator",
    "DevOps Engineer", "Site Reliability Engineer", "Software Developer", "Software Engineer",
    "Application Developer", "Web Developer", "Frontend Developer", "Backend Developer",
    "Full Stack Developer", "Embedded Systems Developer", "Database Administrator", "Data Analyst",
    "Data Engineer", "Data Scientist", "IT Project Manager", "IT Manager", "IT Coordinator",
    "IT Consultant", "Solutions Architect", "Enterprise Architect", "QA Analyst",
    "Test Automation Engineer", "Technical Business Analyst", "IT Compliance Analyst",
    "Technical Account Manager", "Field Support Technician", "IT Trainer", "IT Asset Manager",
    "IT Procurement Specialist", "Incident Response Analyst", "Vulnerability Analyst",
    "Penetration Tester", "SOC Analyst", "IT Auditor", "IT Generalist", "Integration Specialist",
    "CRM Developer", "ERP Analyst", "IT Systems Engineer", "IT Change Manager", "IT Release Manager",
    "Application Support Analyst", "IT Monitoring Specialist", "IT Governance Analyst", "Infrastructure Engineer"
]

pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, job_titles)) + r')\b', flags=re.IGNORECASE)

def keyword_match(text: str) -> bool:
    return bool(pattern.search(text))

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
