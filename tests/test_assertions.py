# Week 8 - Assertion Test

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAssertions:

    # Function to launch Chrome browser
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    # Function to close browser after each session
    def teardown_method(self, method):
        self.driver.quit()

    def test_assert_scenario(self):
        # Navigate to Python's website
        url = "https://www.google.com/"
        self.driver.get(url)

        # Print the link that was used
        print("\nLink Used = " + url)

        # Confirm you are on Python Organization's homepage
        title = self.driver.title
        assert title == "Welcome to Python.org", "\n" + \
            title + " is not Python's homepage! Check your link again."

        # Print Statement confirming  we are on Python Organization page
        print("Python Org homepage has been reached!")

        # Set variables for search box and field element name attributes
        search_box = self.driver.find_element(By.NAME, "q")

        # Enter the search string "asserts"
        search_box.send_keys("asserts")

        # Assert that the desired search string was entered
        assert search_box.get_attribute("value") == "asserts"
