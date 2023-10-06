import time
import Setup
import Test1
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

driver.get(URL)
driver.maximize_window()



# Login
Setup.login(driver, username, password)

# Test1 - Order Clothes and compare price
Test1.purchaseItems(driver)



driver.implicitly_wait(500)
time.sleep(300)