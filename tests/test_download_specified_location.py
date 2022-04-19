# Test Download in Specified Location

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pathlib import Path
import os.path
from selenium.webdriver.common.action_chains import ActionChains
import time


class TestStandardDownload:

    def setup_method(self, method):
        # Create a chrome options object
        self.options = webdriver.ChromeOptions()

        # Specify download directory relative path
        self.download_path = "test_files/"

        # Pull directory of current test script
        self.file_path = os.path.realpath(self.download_path)

        # Specify download directory
        self.preferences = {"download.default_directory": self.file_path}
        # Send preference to ChromeOptions object using experimental option method
        self.options.add_experimental_option("prefs", self.preferences)

        # Launch Chrome browser
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.vars = {}

    # Close browser after each session
    def teardown_method(self, method):
        self.driver.quit()

    # Download in Specified Location
    def test_download_in_specified_location(self):

        # Add a Wait in the event an element is missing
        self.driver.implicitly_wait(7)

        # Navigate to URL
        self.driver.get("http://demo.automationtesting.in/FileDownload.html")

        # Find file creation textbox
        textbox = self.driver.find_element(By.ID, "textbox")

        # Click into the textbox
        self.driver.execute_script("arguments[0].click();", textbox)

        # Enter string in text box
        textbox.send_keys("Test text document.")

        # Find the Generate button
        generate = self.driver.find_element(By.ID, "createTxt")

        # Click on Generate
        self.driver.execute_script("arguments[0].click();", generate)

        # Click on Download link
        download = self.driver.find_element(By.ID, "link-to-download")
        self.driver.execute_script("arguments[0].click();", download)
        time.sleep(2)

        # Get the downloaded file name
        file_name = self.driver.find_element(By.ID, "link-to-download") \
            .get_attribute("download")

        # Get the downloaded file directory
        file_path = self.download_path + file_name
        print("\nFile Directory: ", file_path)

        # Verify the file exists
        file_exists = str(os.path.exists(file_path))
        print("File Exists: ", file_exists)
        assert file_exists == "True"

        # Add TimeSleep to view results
        time.sleep(5)

        # Add Logic to remove the file after test run
        if file_exists:
            os.remove(file_path)
        else:
            print("The file does not exist")
