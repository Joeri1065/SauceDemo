from selenium.webdriver.common.by import By


def login(driver, username, password):
    # Setup
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()

    # Login
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # Verify Login
    try:
        driver.find_element(By.TAG_NAME, "Swag Labs")
    except Exception as e:
        print("Verification failed: ")

def logout(driver):
    # Logout
    driver.find_element(By.ID, "logout").click()

    # Verify logout
    try:
        driver.find_element(By.TAG_NAME, "Swag Labs")
    except Exception as e:
        print("Verification failed: ")