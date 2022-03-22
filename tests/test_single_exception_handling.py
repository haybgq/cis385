# Single Exception Handling

# Import Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_single_exception():
    # Launch Browser
    driver = webdriver.Chrome()

    # Navigate to Amazon
    driver.get("https://www.amazon.com/")

    # Add try-except block
    try:
        # Locate search box
        search_box = driver.find_element(By.ID, "lolnoway")

        # Enter a search string
        search_box.send_keys("Name of the Wind")

    # Handle the error if it is NoSuchElementException by
    # Printing a message
    except NoSuchElementException:
        print("\n Failed to locate search box.")

    # Locate search button
    search_button = driver.find_element(By.ID, "nav-search-submit-button")

    # Click search button
    search_button.click()

    # Assign variable to search string
    search_string = driver.find_element(By.NAME, "field-keywords")

    # Verify that the search string returns expected search criteria
    assert search_string.get_attribute("value") == "Name of the Wind"

    # Exit browser
    driver.quit()
