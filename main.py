from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver (Ensure you have the correct driver installed)
driver = webdriver.Chrome()  # Use the appropriate WebDriver for your browser

# Open the login page
driver.get("https://academy.powerlearnprojectafrica.org/login")  # Replace with the actual login page URL

# Locate username and password fields
username_field = driver.find_element(By.CSS_SELECTOR, "input#email")  # Adjust locator as needed
password_field = driver.find_element(By.NAME, "password")

# Enter valid credentials
username_field.send_keys("your_username")
password_field.send_keys("your_password")
password_field.send_keys(Keys.RETURN)  # Press Enter to submit

# Wait for response and check login success
time.sleep(30)  # Adjust wait time as needed
if "dashboard" in driver.current_url:  # Replace with actual success indicator
    print("Login successful!")
else:
    print("Login failed!")

# Take a screenshot of the result
driver.save_screenshot("login_test_result.png")

# Close the browser
driver.quit()