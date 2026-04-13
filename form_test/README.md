### **Script: `form_test.py`**
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup
url = "https://www.example-site.com/contact"
driver_path = "./chromedriver"  # Update this path

# Initialize ChromeDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url)

def test_required_fields():
    try:
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        errors = driver.find_elements(By.CSS_SELECTOR, ".error-message")
        assert len(errors) > 0, "No validation errors displayed."
        print("PASS: Required field validation works.")
    except Exception as e:
        print(f"FAIL: {e}")
        driver.save_screenshot("validation_error.png")

def test_successful_submission():
    try:
        driver.find_element(By.NAME, "name").send_keys("Test User")
        driver.find_element(By.NAME, "email").send_keys("test@example.com")
        driver.find_element(By.NAME, "message").send_keys("Hello, this is a test.")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".success-message"))
        )
        print("PASS: Form submitted successfully.")
    except Exception as e:
        print(f"FAIL: {e}")
        driver.save_screenshot("submission_error.png")

test_required_fields()
test_successful_submission()
driver.quit()
