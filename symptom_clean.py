import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.firefox.options import Options

# setup
os.chdir("path_to_cwd") # edit here
profile = FirefoxProfile("path_to_profile") # edit here
options = Options()
options.headless = True
driver = webdriver.Firefox(
    executable_path="path_to_geckodriver", # edit here
    options=options,
    firefox_profile=profile
)
driver.get("https://calberkeley.ca1.qualtrics.com/jfe/form/SV_3xTgcs162K19qRv")

# page 1
driver.find_element_by_id("QID1-1-label").click()
driver.find_element_by_id("NextButton").click()

# page 2
WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, "QID10-5-label"))).click()
driver.find_element_by_id("NextButton").click()

# CalNet authentication
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys("username_goes_here") # edit here
driver.find_element_by_id("password").send_keys("password_goes_here") # edit here
driver.find_element_by_id("submit").click()

# page 3
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "QID3-2-label"))).click()
driver.find_element_by_id("QID6-5-label").click()
driver.find_element_by_id("QID17-1-label").click()
driver.find_element_by_id("QID13-2-label").click()
driver.find_element_by_id("NextButton").click()

driver.quit()
