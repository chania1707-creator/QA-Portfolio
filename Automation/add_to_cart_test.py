from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Add first product to cart
driver.find_element(By.CLASS_NAME, "btn_inventory").click()

# Verify cart badge shows 1 item
cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
assert cart_badge == "1", "Cart badge should show 1 item"

driver.quit()
