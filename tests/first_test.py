# Getting Started

# Import appropriate libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time


def test_first_script():

    # 1. Begin the session with Chrome Driver
    driver = webdriver.Chrome()

    # 2. Fetch/Go to Google
    driver.get("https://google.com")

    # 3. Confirm you are on Google
    assert driver.title == "Google"

    # 4. Add an implicit wait to ensure  page load completes
    driver.implicitly_wait(1)

    # 5. Set variables for  search box and field element name attributes
    search_box = driver.find_element(by=By.NAME, value="q")
    search_button = driver.find_element(by=By.NAME, value="btnK")

    # 5. Enter and Search for Selenium string
    search_box.send_keys("Selenium")
    search_button.click()

    # 6. Enter and Search for Selenium string
    search_box = driver.find_element(by=By.NAME, value="q")
    assert search_box.get_attribute("value") == "Selenium"

    # 7. Add sleep to delay browser closer
    time.sleep(2)

    # 8. Exit browser
    driver.quit()
