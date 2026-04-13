from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Setup
url = "https://www.example-site.com/login"
driver_path = "/path/to/chromedriver"  # Update this path
csv_file = "users.csv"

# Initialize ChromeDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Read CSV
users = pd.read_csv(csv_file)

for _, row in users.iterrows():
    username, password, expected = row
    driver.get(url)

    try:
        # Find and fill login form
        user_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        user_field.send_keys(username)

        pass_field = driver.find_element(By.NAME, "password")
        pass_field.send_keys(password)

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Validate result
        if expected == "success":
            assert "Welcome" in driver.page_source, f"Login failed for {username}"
            print(f"PASS: {username} logged in successfully.")
        else:
            assert "Invalid" in driver.page_source, f"Login should have failed for {username}"
            print(f"PASS: {username} login failed as expected.")

    except Exception as e:
        print(f"FAIL: {username} - {e}")
        driver.save_screenshot(f"fail_{username}.png")

driver.quit()