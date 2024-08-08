import logging
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(filename='scraper.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_jobs(unfamiliar_skill):
    # Fetch HTML
    try:
        logging.info(f"Filtering out {unfamiliar_skill}")

        html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text

        # Parse HTML
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

        # Initialize lists
        company_names = []
        skill_list = []
        published_dates = []
        more_info_list = []

        # Extract data
        for job in jobs:
            try:
                published_date = job.find('span', class_="sim-posted").text.replace(' ', '')
                if 'few' in published_date:
                    company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')
                    skills = job.find('span', class_="srp-skills").text.replace(' ', '')
                    more_info = job.header.h2.a['href']

                    if unfamiliar_skill not in skills:
                        company_names.append(company_name.strip())
                        skill_list.append(skills.strip())
                        published_dates.append(published_date.strip())
                        more_info_list.append(more_info.strip())

            except AttributeError:
                continue

        # Create DataFrame and export to Excel
        df = pd.DataFrame({
            'Published Date': published_dates,
            'Company Name': company_names,
            'Required Skills': skill_list,
            'More Information': more_info_list
        })
        df.to_excel('jobs.xlsx', index=False)
        logging.info("Data exported to 'jobs.xlsx'.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        # Ask for the unfamiliar skill once
        print("Input a skill you are not familiar with: ")
        unfamiliar_skill = input('>')
        end_time = datetime.now() + timedelta(minutes=10)
        logging.info("Script started.")
        
        while datetime.now() < end_time:
            logging.info("Running job scrape.")
            scrape_jobs(unfamiliar_skill)
            time.sleep(30)  # Pause for 30 seconds before the next run
        
        logging.info("Script finished.")
    except KeyboardInterrupt:
        logging.info("Script interrupted by user.")
        print("Script interrupted by user.")
