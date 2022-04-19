# Test Drag & Drop

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class TestDragAndDrop:

    # Launch Chrome browser
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    # Close browser after each session
    def teardown_method(self, method):
        self.driver.quit()

    # Drag & Drop test
    def test_drag_and_drop(self):

        # Add a Wait in the event an element is missing
        self.driver.implicitly_wait(7)

        # Navigate to URL
        self.driver.get("https://jqueryui.com/droppable/")

        # Find the source element
        source = self.driver.find_element(By.ID, "draggable")

        # Find the target element
        target = self.driver.find_element(By.ID, "droppable")

        # Create an action chain object
        action = ActionChains(self.driver)

        # Perform the drag and drop from source to target
        action.drag_and_drop(source, target).perform()

        # Add TimeSleep to view results
        time.sleep(5)
