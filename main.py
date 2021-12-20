import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

load_dotenv("G:\My Drive\Programming\Python\EnvironmentVariables\.env.txt")
LINKEDIN_UN = os.getenv("LINKEDIN_UN")
LINKEDIN_PW = os.getenv("LINKEDIN_PW")
LINKED_IN_URL = "https://www.linkedin.com/jobs/search/?currentJobId=2837387292&distance=10&f_E=2&f_JT=F&f_TPR=r2592000&f_WT=1&geoId=103019160&keywords=developer&location=17406%2C%20York%2C%20Pennsylvania%2C%20United%20States&sortBy=R"
chrome_driver_path = "C:\Programming\Web Driver\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(LINKED_IN_URL)

sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

# wait for page load
time.sleep(1)

#enter un and pw. then press enter.
user_id = driver.find_element(By.ID, "username")
user_id.send_keys(LINKEDIN_UN)
password = driver.find_element(By.ID, "password")
password.send_keys(LINKEDIN_PW)
password.send_keys(Keys.ENTER)


job_containers = driver.find_elements(By.CLASS_NAME, "job-card-container")
job_ids = []
for job_container in job_containers:
    job_ids.append(job_container.get_attribute("data-job-id"))
# print(job_ids)

for job_id in job_ids:
    driver.get(f"https://www.linkedin.com/jobs/search/?currentJobId={job_id}&distance=10&f_E=2&f_JT=F&f_TPR=r2592000&f_WT=1&geoId=103019160&keywords=developer&location=17406%2C%20York%2C%20Pennsylvania%2C%20United%20States&sortBy=R")
    time.sleep(3)
    # print(driver.page_source)
    save = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
    save.click()
    right_rail = driver.find_element(By.CLASS_NAME, "jobs-search__right-rail")
    right_rail.click()
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.END)
    time.sleep(3)
    try:
        follow = right_rail.find_element(By.CSS_SELECTOR, 'button.follow')
        follow.click()
    except NoSuchElementException:
        continue


# jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-list__title")
# for job in jobs:
#     job.click()
#     save = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
#     save.click()
#     time.sleep(1)
    # right_rail = driver.find_element(By.CLASS_NAME, "jobs-search__right-rail")
    # right_rail.click()
    # html = driver.find_element(By.TAG_NAME, "html")
    # html.send_keys(Keys.END)
    # follow = driver.find_element(By.CSS_SELECTOR, 'button.follow')
    # print(follow.text)
    # follow.click()
