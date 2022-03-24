# Multiple Exceptions Handling

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
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")

        # Enter a search string
        search_box.send_keys("Name o'the Wind")

        # Assign variable to search string
        search_string = driver.find_element(By.NAME, "lolnoway")

        # Verify that the search string returns expected search criteria
        book_title = search_string.get_attribute("value")
        assert book_title == "Name of the Wind"

    # Handle the AssertionError by showing the expected book title.
    except AssertionError:
        print("\nAssertion failed. " + book_title + " is not the correct book "
                                                    "title. The correct title "
                                                    "should be Name of the Wind."
              )

    # Handle the NoSuchElementException by notifying user of missing element.
    except NoSuchElementException:
        print("\nFailed to locate search string element.")

    # Locate search button
    search_button = driver.find_element(By.ID, "nav-search-submit-button")

    # Click search button
    search_button.click()

    # Exit browser
    driver.quit()
