import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# Static data
driver=webdriver.Chrome()
URL="https://saucedemo.com"
username="standard_user"
password="secret_sauce"
wait = WebDriverWait(driver, 10)

# Setup
driver.get(URL)
driver.maximize_window()

# Login
driver.find_element(By.ID, "user-name").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "login-button").click()


driver.implicitly_wait(5)
time.sleep(30)