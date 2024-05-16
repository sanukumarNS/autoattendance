# google_search.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def google_search(query):
    # Configure WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run headless Chrome
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    try:
        # Go to Google
        driver.get('https://www.google.com')

        # Locate the search box, enter the query, and submit
        search_box = driver.find_element(By.NAME, 'q')
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Wait for results to load
        time.sleep(5)

        # Print the title of the first search result
        first_result = driver.find_element(By.CSS_SELECTOR, 'h3')
        print("First result title: ", first_result.text)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    google_search('GitHub Actions')
