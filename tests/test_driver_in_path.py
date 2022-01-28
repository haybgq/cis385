# Report 2 - Automation Script Ran w/Driver in PATH

# Import Libraries
import pytest
from selenium import webdriver
import time


def test_chrome_with_driver_in_path():
    # Create Driver Instance & Launch Browser
    driver = webdriver.Chrome()

    # Go to Syllabus Website
    driver.get("https://syllabi.readthedocs.io/en/latest/CIS-385.html")

    # Confirm We Are on Correct Page
    assert driver.title == "CIS 385 Capstone — Syllabi Spring 2022 documentation"

    # Add sleep to delay browser closer
    time.sleep(2)

    # Exit browser
    driver.quit()
