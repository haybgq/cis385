# Test Standard Upload

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os


class TestStandardUpload:

    # Launch Chrome browser
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    # Close browser after each session
    def teardown_method(self, method):
        self.driver.quit()

    # Standard Upload test
    def test_standard_upload(self):
        # Add a Wait in the event an element is missing
        self.driver.implicitly_wait(7)

        # Navigate to URL
        self.driver.get("http://demo.automationtesting.in/FileUpload.html")

        # Specify upload directory relative path
        upload_file_path = "test_files/testPDF.pdf"

        # Pull directory of current test script
        file_path = os.path.realpath(upload_file_path)

        # Find Browse Files button
        browse_files = self.driver.find_element(By.ID, "input-4")

        # Upload the file
        browse_files.send_keys(file_path)

        # Find Upload button
        upload_button = self.driver.find_element(By.CSS_SELECTOR, ".fileinput-upload "
                                                                  "> .hidden-xs")

        # Click Upload Button
        self.driver.execute_script("arguments[0].click();", upload_button)

        # Add TimeSleep to view results
        time.sleep(5)
