# Test Radio Button Selection

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class TestRadioButtonSelection:

    # Launch Chrome browser
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    # Close browser after each session
    def teardown_method(self, method):
        self.driver.quit()

    # Radio Button Selection
    def test_radio_button_selection(self):

        # Add a Wait in the event an element is missing
        self.driver.implicitly_wait(5)

        # Navigate to practice form URL
        self.driver.get("https://demoqa.com/automation-practice-form")

        # Enter first & last Name
        self.driver.find_element(By.ID, "firstName").send_keys("Test")
        self.driver.find_element(By.ID, "lastName").send_keys("Tester")

        # 8 Provide user email
        self.driver.find_element(By.ID, "userEmail").send_keys("test@test.com")

        # Find and assign a variable to the female radio button option
        radio_button_female = self.driver.find_element(By.CSS_SELECTOR
                                                       , ".custom-radio:"
                                                         "nth-child(2) > "
                                                         ".custom-control-label"
                                                       )

        # Add conditional logic to handle selection of the radio button as follows:
        # If radio button is not displayed, stop the test and print message to
        # notify user:
        if not radio_button_female.is_displayed():
            assert radio_button_female.is_displayed(), "\n'Gender = Female' " \
                                                       "radio button is not " \
                                                       "visible."

        # Else if radio button is displayed, but not enabled, stop the test and
        # print message to notify user
        elif radio_button_female.is_displayed() & \
                (not radio_button_female.is_enabled()):
            assert radio_button_female.is_enabled(), "\n'Gender = Female' " \
                                                     "radio not enabled."

        # Else, click on the radio button and verify that it is selected
        else:
            radio_button_female.click()

            # Because a different element registers the radio button selection,
            # we shall use a different element to validate the selection:
            selected_radio_button_female = self.driver.find_element(By.ID,
                                                                    "gender-radio-2")
            assert selected_radio_button_female.is_selected(), "\n'Gender = " \
                                                               "Female' radio " \
                                                               "cannot be " \
                                                               "selected at this " \
                                                               "time. "
