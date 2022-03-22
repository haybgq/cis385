# Explicit Wait

# Import Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


def test_scenario_3():
    # Launch Browser
    driver = webdriver.Chrome()

    # Navigate to Google
    driver.get("https://google.com")

    # Confirm you are on the correct page
    assert driver.title == "Google"

    # Wait for Search Box element to appear for 10 seconds
    # If successful, retrieve the element
    try:
        search_box = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.NAME, "x")))

        # Locate search button
        search_button = driver.find_element(By.NAME, value="btnK")

        # Interact with the Elements - Enter and Search for Selenium string
        search_box.send_keys("Selenium")
        search_button.click()

    except TimeoutException:
        print("\n Failed to locate search box.")

    finally:
        # Exit browser
        driver.quit()
