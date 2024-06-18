#!/usr/bin/python3
# web_scrap_emails_from_europarl.py
# Author: Luca Soler <luca.soler@edu.ece.fr>
# Description: Ce script récupère les adresses email des membres du Parlement européen depuis une page donnée (ici pour les députés français).
#              Il parcourt les profils des membres et extrait les adresses email disponibles.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import shutil


def get_emails_from_europarl(url):
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = (
        shutil.which("google-chrome")
        or shutil.which("chromium-browser")
        or shutil.which("chromium")
    )

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)

        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "a.erpl_member-list-item-content")
            )
        )

        profile_links = driver.find_elements(
            By.CSS_SELECTOR, "a.erpl_member-list-item-content"
        )

        for link in profile_links:
            profile_url = link.get_attribute("href")
            if profile_url:
                driver.execute_script(
                    "window.open(arguments[0], '_blank');", profile_url
                )
                driver.switch_to.window(driver.window_handles[-1])

                email = get_email_from_profile(driver)
                if email:
                    print(email.split(":")[1])

                driver.close()
                driver.switch_to.window(driver.window_handles[0])

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
    finally:
        driver.quit()


def get_email_from_profile(driver):
    try:
        email_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.link_email"))
        )
        return email_element.get_attribute("href")
    except Exception as e:
        print(f"Impossible de trouver l'email : {e}")
        return None


if __name__ == "__main__":
    url = "https://www.europarl.europa.eu/meps/en/search/advanced?name=&euPoliticalGroupBodyRefNum=&countryCode=FR&bodyType=ALL&bodyReferenceNum="
    get_emails_from_europarl(url)
