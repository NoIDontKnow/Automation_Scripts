from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
search_query = "wireless headphones"
url = "https://www.example-ecommerce-site.com"
driver_path = "/path/to/chromedriver"  # Update this path

# Initialize ChromeDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url)

try:
    # Find search box and enter query
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys(search_query + Keys.RETURN)

    # Wait for results
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".product-item"))
    )

    # Validate results
    results = driver.find_elements(By.CSS_SELECTOR, ".product-item")
    print(f"Found {len(results)} results for '{search_query}'.")

    # Take screenshot
    driver.save_screenshot("search_results.png")
    print("Test passed: Search results validated.")

except Exception as e:
    print(f"Test failed: {e}")
    driver.save_screenshot("error_screenshot.png")

finally:
    driver.quit()