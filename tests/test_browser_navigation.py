# Test Browser Navigation

# Import Libraries
import pytest
from selenium import webdriver


def test_browser_navigation():
    # Create Driver Instance & Launch Chrome Browser
    driver = webdriver.Chrome()

    # Navigating to a website
    driver.get("https://selenium.dev")

    # Pressing the Back button
    driver.back()

    # Pressing the Forward button
    driver.forward()

    # Refreshing the page
    driver.refresh()

    # Closing the window
    driver.quit()
