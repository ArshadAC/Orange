import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://automation.credence.in")
driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
driver.find_element(By.ID,"email").send_keys("Rajeshp@gmail.com")
driver.find_element(By.ID,"password").send_keys("Rajesh@123")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(5)

# Validate Login
try:
    driver.find_element(By.XPATH,"//h2[normalize-space()='CredKart']")
    print("Login pass")
except:
    print("Login failed")