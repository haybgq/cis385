# Test Standard Download

from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
import os.path
from selenium.webdriver.common.action_chains import ActionChains
import time


class TestStandardDownload:

    # Launch Chrome browser
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    # Close browser after each session
    def teardown_method(self, method):
        self.driver.quit()

    # Standard Download test
    def test_standard_download(self):

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

        # Get the 'Downloads' folder path
        downloads_path = str(Path.home() / "Downloads")

        # Get the downloaded file directory
        file_path = downloads_path + "/" + file_name
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
