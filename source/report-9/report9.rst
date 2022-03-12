**Author**: *Guy Sinarinzi-Hay*

**Posted**: *3/12/22*

Report 9: Selenium WebDriver - Waits
====================================

This report covers activities performed between 3/8/22 - 3/12/22. There are
instances in test automation where a page, and by association, an element, will
not be present when we expect it due to page load delays. Such instances are
addressed by adding Waits.

.. contents:: Contents:
   :depth: 3
   :local:

.. _overview9:

Overview
--------

Modern web pages tend to load asynchronously, meaning that rather than execute
page load in an orderly fashion, example: *blocking the page content from
loading until a JavaScript file is downloaded and ran*, both the code and page
content will be processed simultaneously. In other words, the browser will not
have a downtime during asynchronous loading, given that it will be performing
other tasks. This approach reduces load times and improves performance.

Many web applications rely on asynchronous loading for their web pages,
which results in elements on the page being loaded at different time intervals
every time the browser loads the page. This makes the process of locating
elements during test automation difficult, as they are sometimes not yet in the
Document Object Model (DOM), and will result in an exception being raised.
Using Waits solves this issue by adding a delay or slack between actions
performed, especially when trying to locate an element. If an element is located
before the allotted wait time, then the execution flow continues.

.. _wait types:

Types of Waits
--------------

Waits can be broken down into two categories: Implicit and Explicit Waits.

.. _implicit wait:

Implicit Waits
^^^^^^^^^^^^^^

Implicit waits will poll the DOM for a given amount of time when attempting to
locate elements or execute a command. The implicit wait is usually set right
after the the browser is launched, and runs for the life of the session. The
following syntax is used to denote an implicit wait:

.. code-block:: Python

   driver.implicitly_wait(time_in_seconds)


The test script below shows the application of an implicit wait.
Should an element not be found, the session will wait 10 seconds before raising
a ``NoSuchElement`` exception:

.. literalinclude:: ../../tests/test_element_interaction.py
   :linenos:
   :lines: 1-36
   :emphasize-lines: 15-16
   :caption: Implicit Wait

.. _explicit wait:

Explicit Waits
^^^^^^^^^^^^^^

Unlike implicit waits that apply to all elements in a given execution flow,
explicit waits apply only to the elements for which they are exclusively defined.
They allow the execution flow to proceed if an expected condition is satisfied,
otherwise, a ``TimeOutException`` is thrown. Explicit waits require a few
configurations before they can be applied to a script.

First, we have to import the ``WebDriverWait`` class which sets the wait time:

.. code-block:: Python

   from selenium.webdriver.support.ui import WebDriverWait

Then, import the ``expected_conditions`` class that sets the condition we
wish to verify:

.. code-block:: Python

   from selenium.webdriver.support import expected_conditions

Below are some common conditions that can be used from this class:

.. csv-table:: Expected Conditions [#f1]_
   :file: ../files/se-webd-expected-conditions.csv
   :widths: auto
   :header-rows: 1

Our explicit wait can then be written as follows (in this example, we used the ``presence_of_element_located(locator)``
condition):

.. code-block:: Python

   WebDriverWait(driver, time_in_seconds).until(
                                expected_condition.presence_of_element_located
                                ((By.NAME, "name")))

The test script below demonstrates the use of an explicit wait where we look for
the search box element, and if it cannot be found, we handle the
``TimeOutException`` error:

.. literalinclude:: ../../tests/test_explicit_wait.py
   :linenos:
   :emphasize-lines: 24-25
   :caption: Explicit Wait

.. _time delay:

Time Delay
----------

Another method used to pause the execution flow is known as *Sleep Time*. This
method is used to suspect the execution of a session for a given number of
seconds. To use sleep time, we must first import the ``time`` module as
follows:

.. code-block:: Python

   import time

Then, we make a call to the sleep function and pass an argument in seconds:

.. code-block:: Python

   time.sleep(time_in_seconds)

This can be demonstrated in the test case below, where the sleep timer is set to
a 2-second wait before letting the execution flow resume:

.. literalinclude:: ../../tests/test_driver_in_path.py
   :linenos:
   :emphasize-lines: 19-20
   :caption: Time Sleep

It should be noted that while sleep time is a type of wait, there is a
difference between it and the implicit and explicit waits. The ``time.sleep()``
feature will halt the execution for a stated amount of time, regardless of
whether or not an element is found. Implicit and Explicit waits will resume the
execution flow if an element is found before the stated wait time is over.

Therefore, using ``time.sleep`` is considered a bad testing practice as it
affects performance and delays execution where implicit and explicit waits would
have sufficed.

.. _time spent9:

Breakdown of Time Spent
-----------------------

**Total Hours**: **12 hours**

* **Tuesday, 3-8-2022**: 3 hours
   * Created Report 9
   * Added Overview documentation
   * Researched Types of Waits

* **Wednesday, 3-9-2022**: 3 hours
   * Researched Implicit Waits.
   * Added Implicit Wait documentation and tests.
   * Researched Explicit Waits.

* **Friday, 3-11-2022**: 4.5 hours
   * Added Explicit Wait documentation and tests.
   * Added finishing touches to Report 9 documentation.
   * Demoed work to Dr. Craven.

* **Saturday, 3-12-2022**: 1.5 hour
   * Added Time Delay documentation and tests.
   * Made updates based on feedback from Dr. Craven.
   * Pushed all changes to GitHub.

.. _references9:

References
----------

* `Link to test cases on GitHub <https://github.com/haybgq/cis385/tree/main/tests>`_
* `Link to Waits documentation <https://selenium-python.readthedocs.io/waits.html>`_
* `Link to Time Sleep documentation <https://docs.python.org/2/library/time.html#time.sleep>`_

.. rubric:: Footnotes:
.. [#f1] Selenium. (2011). Selenium WebDriver Support Expected Conditions.
   Retrieved March 11, 2022, from `Selenium Expected Conditions <https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html>`_
