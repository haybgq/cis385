# Week 8 - Test without Assertion

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWithoutAssertions:

    # Function to launch Chrome browser
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    # Function to close browser after each session
    def teardown_method(self, method):
        self.driver.quit()

    def test_navigate_to_page(self):
        # Navigate to Python's website
        url = "https://www.python.org/"
        self.driver.get(url)

        # Print the link that was used
        print("\nLink Used = " + url)

        # Print Statement confirming  we are on Python Organization page
        print("Python Org homepage has been reached!")

        # Set variables for search box and field element name attributes
        search_box = self.driver.find_element(By.NAME, "q")

        # Enter the search string "asserts"
        search_box.send_keys("asserts")

