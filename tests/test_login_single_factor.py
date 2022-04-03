# Test Single-Factor Login

"""
Make sure the app.py script is executed so the flask server is running -
else this script will fail.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginSingleFactor:

    # Launch Chrome browser
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    # Close browser after each session
    def teardown_method(self, method):
        self.driver.quit()

    # Login Scenario
    def test_single_factor(self):

        # Link & Login Credentials
        url = "http://127.0.0.1:5000/"
        username = "thatProfessor"
        password = "isCraven"

        # Add a Wait in the event an element is missing
        self.driver.implicitly_wait(5)

        # Navigate to Homepage
        self.driver.get(url)

        # Click on Login link to redirect to Login page
        self.driver.find_element(By.LINK_TEXT, "login").click()

        # Find username input field and insert the username
        self.driver.find_element(By.ID, "username").send_keys(username)

        # Find password input field and insert password
        self.driver.find_element(By.ID, "password").send_keys(password)

        # Click login button
        self.driver.find_element(By.ID, "submit").click()

        # Validate the credentials entered are valid
        valid_credentials = self.driver.find_element(By.ID, "alert")\
            .get_attribute("innerHTML")
        assert valid_credentials.strip() == "Your credentials are valid!"
