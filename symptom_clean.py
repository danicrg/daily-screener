import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.firefox.options import Options

import config


# setup
os.chdir(config.PATH_TO_CWD)
profile = FirefoxProfile(config.PATH_TO_PROFILE)
options = Options()
options.headless = True
driver = webdriver.Firefox(
    executable_path=config.PATH_TO_DRIVER,
    options=options,
    firefox_profile=profile
)
driver.get("https://calberkeley.ca1.qualtrics.com/jfe/form/SV_3xTgcs162K19qRv")

# page 1
WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "QID1-1-label"))).click()
driver.find_element_by_id("NextButton").click()

# page 2
WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "QID10-5-label"))).click()
driver.find_element_by_id("NextButton").click()

# CalNet authentication
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(config.USERNAME)
driver.find_element_by_id("password").send_keys(config.PASSWORD)
driver.find_element_by_id("submit").click()

# page 3
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "QID3-2-label"))).click()
driver.find_element_by_id("QID6-5-label").click()
driver.find_element_by_id("QID17-1-label").click()
driver.find_element_by_id("QID13-2-label").click()
driver.find_element_by_id("NextButton").click()

driver.quit()
