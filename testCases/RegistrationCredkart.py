import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://automation.credence.in/register")
driver.find_element(By.XPATH,"//a[normalize-space()='Register']")
driver.find_element(By.ID,"name").send_keys('Rajesh')
driver.find_element(By.ID,"email").send_keys('Rajeshp@gmail.com')
driver.find_element(By.ID,"password").send_keys("Rajesh@123")
driver.find_element(By.ID,"password-confirm").send_keys("Rajesh@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)

# Validate Registration
try:
    driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
    print("Registration Pass")
except:
    print("Registration Fail")
