import time
from selenium.webdriver.common.by import By


def purchaseItems(driver):
    firstName = "John"
    lastName = "Doe"
    postalCode = "12345"

    #Select backpack
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    Price_Backpack=driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(Price_Backpack)

    #Select bike light
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    # Navigate to shopping cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Check out
    driver.find_element(By.ID, "checkout").click()

    # Fill out shipping information
    driver.find_element(By.ID, "first-name").send_keys(firstName)
    driver.find_element(By.ID, "last-name").send_keys(lastName)
    driver.find_element(By.ID, "postal-code").send_keys(postalCode)

    # Save order data
    order_total_without_tax=driver.find_element(By.CLASS_NAME, "order_total").text
    price_tax=driver.find_element(By.CLASS_NAME, "summary_tax_label").text
    order_total_with_tax=driver.find_element(By.CLASS_NAME, "summary_total_label").text


    # Confirm order
    driver.find_element(By.ID, "continue").click()


    # Validate order totals
    order_total_with_tax2=driver.find_element(By.CLASS_NAME, "summary_total_label")


    if order_total_without_tax==order_total_without_tax2:
        print("Order total without tax is correct: ", order_total_without_tax)
    else:
        print("Order total without tax is incorrect: ", order_total_without_tax)

    # Confirm order
        driver.find_element(By.ID, "finish").click()