**Author**: *Guy Sinarinzi-Hay*

**Posted**: *2/7/22*

Report 4: Browser & Elements
============================

This report covers activities performed between 1/29/22 - 2/6/22. So far, we
have explored setting up selenium webdriver and configuring browser driver. This
topic explores the activities that occur on the browser side of automation,
including:

* Browser Navigation Commands
* Identifying Elements on a Page (Locators)
* Interacting with the Elements
* Example Test Cases

.. _browser navigation:

Browser Navigation
------------------

The Selenium WebDriver :ref:`architecture <selenium webdriver>` diagram
shows browsers as the third layer of automation. All key
automation functions happen on the browser side, which then relays status
reports back to the WebDriver with each test iteration. The browser is the
medium in which all automation activities occur.

In :ref:`Configuration <configuration>`, we learned the command to launch a
browser-instance via the browser-driver (example: ``chromedriver``). Once the
browser is up and running, there are basic navigation commands we can use as
follows:

* Navigating to a website
* Pressing the Back button
* Pressing the Forward button
* Refreshing the page
* Closing the window

An example of these navigation commands can be seen below:

.. literalinclude:: ../../tests/test_browser_navigation.py
   :linenos:
   :caption: Script for Browser Navigation

.. _locator strategies:

Identifying Elements on a Page
-------------------------------

In web automation, we interact with an web application via the use of elements
located on that page. Locators serve the purpose of identifying elements on the
page, and then passing the argument to the ``find_element`` method as follows:

.. code-block:: Python

    # Name and CSS_Selector locators:
    driver.find_element(By.NAME, value="elementName")
    driver.find_element(By.CSS_SELECTOR, ".form-control")

Below is a list of current locators used in Selenium WebDriver:

.. csv-table:: Current Locators [#f1]_
   :file: ../files/se-wedb-locators.csv
   :widths: auto
   :header-rows: 1

An example of these locators in use can be found in :ref:`lines 26-27, 49 and 61 <source code4>`
of the source code.

Interacting with the Elements
------------------------------

When we have identified the elements, we then proceed to
interact with by adding an interaction command as follows:

.. code-block:: Python

    # Click and SendKeys commands:
    search_button.click()
    search_box.send_keys("Selenium")

Below is a list of current interaction commands used in Selenium WebDriver:

.. csv-table:: Current Interaction Commands [#f2]_
   :file: ../files/se-wedb-interactors.csv
   :widths: auto
   :header-rows: 1

An example of these interactions in use can be found in :ref:`lines 30-31, 52 and 58 <source code4>`
of the source code.

.. _source code4:

.. literalinclude:: ../../tests/test_element_interaction.py
   :emphasize-lines: 25-27, 29-31, 47-49, 51-52, 57-58, 60-61
   :linenos:
   :caption: Script for Element Find and Interaction

.. _time spent4:

Breakdown of Time Spent
-----------------------

**Total Hours**: **14 hours**

* **Monday, 1-31-2022**: 1 hour
   * Setup initial documentation for Report 4.

* **Wednesday, 2-2-2022**: 2 hours
   * Researched browser navigation commands.
   * Added notes to page.

* **Thursday, 2-3-2022**: 4 hours
   * Added example script for browser navigation.
   * Researched element locator and interactions.
   * Added element notes to Report 4 page.

* **Friday, 2-4-2022**: 4 hours
   * Added scripts for element interaction and locators.
   * Edited notes for browser navigation section.
   * Did a Report 4 demo with Dr. Craven.

* **Sunday, 2-6-2022**: 3 hours
   * Updated Report 4 based on feedback comments from Dr. Craven.
   * Pushed all changes to GitHub.


References
----------

* `Link to the code on GitHub <https://github.com/haybgq/cis385>`_
* `Link to Locator Strategies <https://www.selenium.dev/documentation/webdriver/elements/locators/>`_
* `Link to Interacting with Web Elements <https://www.selenium.dev/documentation/webdriver/elements/interactions/>`_

.. rubric:: Footnotes:
.. [#f1] Locator strategies. Traditional Locators. Selenium. (2022, January 12).
   Retrieved February 4, 2022, from https://www.selenium.dev/documentation/webdriver/elements/locators/#traditional-locators
.. [#f2] Locator strategies. Interacting with web elements. Selenium. (2022, January 17).
   Retrieved February 4, 2022, from https://www.selenium.dev/documentation/webdriver/elements/interactions/