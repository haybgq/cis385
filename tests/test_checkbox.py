# Test Checkbox Selection

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class TestCheckboxSelection:

    # Launch Chrome browser
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    # Close browser after each session
    def teardown_method(self, method):
        self.driver.quit()

    # Checkbox Selection
    def test_checkbox_selection(self):
        # Add a Wait in the event an element is missing
        self.driver.implicitly_wait(5)

        # Navigate to practice form URL
        self.driver.get("https://demoqa.com/automation-practice-form")

        # Enter first & last Name
        self.driver.find_element(By.ID, "firstName").send_keys("Test")
        self.driver.find_element(By.ID, "lastName").send_keys("Tester")

        # Provide user email
        self.driver.find_element(By.ID, "userEmail").send_keys("test@test.com")

        # Find and assign a variable to the female radio button option
        radio_button_female = self.driver.find_element(By.CSS_SELECTOR
                                                       , ".custom-radio:"
                                                         "nth-child(2) > "
                                                         ".custom-control-label"
                                                       )
        # Click on the radio button
        radio_button_female.click()

        # verify that radio button was selected
        selected_radio_button_female = self.driver.find_element(By.ID,
                                                                "gender-radio-2")
        assert selected_radio_button_female.is_selected(), "\n'Gender = " \
                                                           "Female' radio " \
                                                           "cannot be " \
                                                           "selected at this " \
                                                           "time. "
        # Enter phone number
        self.driver.find_element(By.ID, "userNumber").send_keys("1234567890")

        # Assign Variables to Checkbox options
        sports_checkbox = self.driver.find_element(By.CSS_SELECTOR,
                                                   ".custom-checkbox:nth-child(1) >"
                                                   " .custom-control-label")
        music_checkbox = self.driver.find_element(By.CSS_SELECTOR,
                                                  ".custom-checkbox:nth-child(3) >"
                                                  " .custom-control-label")

        # Add conditional logic to handle selection of the checkboxes as follows:
        # If checkboxes are not displayed, stop the test and print message to
        # notify user:
        if (not sports_checkbox.is_displayed()) or (not music_checkbox.is_displayed()):

            # Add nested IF statement to identify which element is not displayed:
            if not sports_checkbox.is_displayed():
                assert sports_checkbox.is_displayed(), "\n'Hobby = Sports' " \
                                                       "checkbox is not visible."
            elif not music_checkbox.is_displayed():
                assert music_checkbox.is_displayed(), "\n'Hobby = Music' " \
                                                      "checkbox is not visible."
            else:
                assert sports_checkbox.is_displayed(), "\n'Hobby = Sports' " \
                                                       "checkbox is not visible."
                assert music_checkbox.is_displayed(), "\n'Hobby = Music' " \
                                                      "checkbox is not visible."

        # Else if either checkboxes are disabled, stop the test and notify user:
        elif (not sports_checkbox.is_enabled()) or (not music_checkbox.is_enabled()):

            # Add nested IF statement to identify which element is not enabled:
            if not sports_checkbox.is_enabled():
                assert sports_checkbox.is_enabled(), "\n'Hobby = Sports' " \
                                                     "checkbox is not enabled."
            elif not music_checkbox.is_enabled():
                assert music_checkbox.is_enabled(), "\n'Hobby = Music' " \
                                                    "checkbox is not enabled."
            else:
                print("Both of your checkbox options are not enabled!")

        # Else, click both checkboxes and validate that they are selected:
        else:
            # Use JavaScript to perform click and avoid obscuring elements
            self.driver.execute_script("arguments[0].click();", sports_checkbox)
            select_sports_checkbox = self.driver.find_element(By.ID,
                                                              "hobbies-checkbox-1")
            assert select_sports_checkbox.is_selected(), "\n'Hobby = " \
                                                         "Sports' checkbox" \
                                                         "cannot be " \
                                                         "selected at this " \
                                                         "time. "

            # Use JavaScript to perform click and avoid obscuring elements
            self.driver.execute_script("arguments[0].click();", music_checkbox)
            select_music_checkbox = self.driver.find_element(By.ID,
                                                             "hobbies-checkbox-3")
            assert select_music_checkbox.is_selected(), "\n'Hobby = " \
                                                        "Music' checkbox" \
                                                        "cannot be " \
                                                        "selected at this " \
                                                        "time. "
