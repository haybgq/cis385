# Element Interaction

# Import appropriate libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time


def test_scenario_1():
    # Launch Browser
    driver = webdriver.Chrome()

    # Wait for up to 10 seconds for elements to load on page
    driver.implicitly_wait(10)

    # Navigate to Google
    driver.get("https://google.com")

    # Confirm you are on the correct page
    assert driver.title == "Google"

    # Find Elements
    search_box = driver.find_element(By.NAME, value="q")
    search_button = driver.find_element(By.NAME, value="btnK")

    # Interact with the Elements - Enter and Search for Selenium string
    search_box.send_keys("Selenium")
    search_button.click()

    # Add sleep to allow page elements to load
    time.sleep(2)

    # Exit browser
    driver.quit()


def test_scenario_2():
    # Launch Chrome Browser
    driver = webdriver.Chrome()

    # Navigate to Selenium Website
    driver.get("https://www.selenium.dev/")

    # Find search-box (using locator = CSS_Selector)
    # Click to select search box (using interaction command  = click)
    driver.find_element(By.CSS_SELECTOR, ".form-control").click()

    # Search for the word "elements" & (using interaction command  = send_keys)
    driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys("elements")

    # Add sleep to temporarily suspend the execution.
    time.sleep(1)

    # Press Enter (using interaction command  = send_keys)
    driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys(Keys.ENTER)

    # Find link to 'Finding web Elements' and select it
    driver.find_element(By.LINK_TEXT, "Finding web elements").click()

    # Confirm you are on the right page
    assert driver.title == "Web elements | Selenium"

    # Exit Browser
    driver.quit()
