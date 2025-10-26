import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def job():
    try:
        path = r"C:\chromedriver-win64\chromedriver.exe"
        service = Service(executable_path=path)
        driver = webdriver.Chrome(service=service)

        all_titles = []
        all_descriptions = []
        all_new_links = []

        nb_page = 1
        while nb_page <= 10:
            url = f"https://www.thesun.co.uk/sport/boxing/page/{nb_page}/"
            driver.get(url)
            logging.info(f"Scraping page {nb_page}: {url}")

            containers = driver.find_elements(By.XPATH, '//div[@class="teaser__copy-container"]')
            if not containers:
                logging.info("No more articles found. Stopping scraping.")
                break

            for container in containers:
                try:
                    title = container.find_element(By.XPATH, './a/span').text
                    description = container.find_element(By.XPATH, './a/h3').text
                    new_link = container.find_element(By.XPATH, './a').get_attribute('href')
                    all_titles.append(title)
                    all_descriptions.append(description)
                    all_new_links.append(new_link)
                except Exception as e:
                    logging.error(f"Error extracting data from container: {e}")

            nb_page += 1
            time.sleep(5)  

        now = datetime.now()
        dd_mm_yyyy = now.strftime("%d-%m-%Y")
        df_headLine = pd.DataFrame({
            'title': all_titles,
            'description': all_descriptions,
            'new_link': all_new_links
        })
        name_file = fr'C:\Users\lenovo\Documents\freelance job\data_engineer\autoamtion_data_selenium\project_1\boxing_news_{dd_mm_yyyy}.csv'
        df_headLine.to_csv(name_file, index=False)
        logging.info(f"Data saved to {name_file}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        driver.quit()
        logging.info("ChromeDriver closed.")

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', hour=14, minute=37, second=40) 
    logging.info("Scheduler started. Waiting for the scheduled time...")
    scheduler.start()