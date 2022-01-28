# Report 2 - Automation Script Ran w/Driver Manager

# Import Libraries
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_chrome_with_driver_manager():

    # Check for Driver Updates & Launch Chrome
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Go to Syllabus Website
    driver.get("https://syllabi.readthedocs.io/en/latest/CIS-385.html")

    # Confirm We Are on Correct Page
    assert driver.title == "CIS 385 Capstone — Syllabi Spring 2022 documentation"

    # Add sleep to delay browser closer
    time.sleep(2)

    # Exit browser
    driver.quit()
