# Report 2 - Automation Script Ran w/Driver Location Specified

# Import Libraries
import pytest
from selenium import webdriver
import time


def test_chrome_with_driver_location_specified():
    # Assign Driver Location
    driver_path = "../driver/chrome/current/chromedriver"

    # Windows Users - Use Raw Switch for Driver Location
    # driver_path = r'../driver/chrome/current/chromedriver'

    # Create Driver Instance & Launch Browser
    driver = webdriver.Chrome(driver_path)

    # Go to Syllabus Website
    driver.get("https://syllabi.readthedocs.io/en/latest/CIS-385.html")

    # Confirm We Are on Correct Page
    assert driver.title == "CIS 385 Capstone — Syllabi Spring 2022 documentation"

    # Add sleep to delay browser closer
    time.sleep(2)

    # Exit browser
    driver.quit()
