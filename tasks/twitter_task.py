# backend/tasks/twitter_task.py

from time import sleep
import os
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

def perform_twitter_task(url: str):
    print(f"🔁 Performing Twitter task at {url}")
    driver = uc.Chrome(headless=True)
    driver.get("https://twitter.com/login")

    sleep(2)
    driver.find_element(By.NAME, "text").send_keys(os.getenv("TWITTER_USER"))
    driver.find_element(By.TAG_NAME, "button").click()
    sleep(2)

    driver.find_element(By.NAME, "password").send_keys(os.getenv("TWITTER_PASS"))
    driver.find_element(By.TAG_NAME, "button").click()
    sleep(4)

    driver.get(url)
    sleep(5)
    # Add retweet, like, or follow detection logic here
    driver.quit()
