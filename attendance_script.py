# attendance_script.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def log_attendance():
    # Configure WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run headless Chrome
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    try:
        # Open the login page
        driver.get('https://company-website.com/login')

        # Locate and fill the username and password fields
        username = driver.find_element(By.NAME, 'username')
        password = driver.find_element(By.NAME, 'password')
        username.send_keys('your_username')
        password.send_keys('your_password')

        # Submit the login form
        password.send_keys(Keys.RETURN)

        # Wait for login to complete (you may need to adjust the wait time)
        time.sleep(5)

        # Navigate to the attendance page
        driver.get('https://company-website.com/attendance')

        # Perform the action to log attendance (this part will depend on the specific website)
        log_button = driver.find_element(By.ID, 'log_button')  # Adjust the selector
        log_button.click()

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    log_attendance()
