**Author**: *Guy Sinarinzi-Hay*

**Posted**: *1/19/22*

Report 1 & 2: Getting Started
=============================

This report covers activities performed between 1/10/22 - 1/19/22. This section
covers the process of setting up the tools you will need to begin automation.
Contents include:

* Setup
* First Test Case

.. _setup:

Setup
-----

To get started, access the ``readme.rst`` file on `GitHub <https://github.com/haybgq/cis385/blob/main/readme.rst>`__
and follow the steps outlined in the document.

.. literalinclude:: ../../readme.rst
   :language: rst
   :linenos:
   :caption: readme.rst

By the end of the installation, we should have:

1. Selenium installed.
2. pyTest installed.
3. The latest browser webdriver installed.

In order to create and execute successful automation tests, we will download and
configure the tools below:

.. _selenium webdriver:

* **Selenium WebDriver**: A core component of the overall Selenium framework,
  it is an open-source tool that allows for the automation of user-facing web
  applications such as Linux, Mac and Windows. As a collection of open-source
  APIs Selenium WebDriver performs web testing across browsers such as Chrome,
  Safari, Edge, etc. WebDriver works by opening a browser, identifying
  browser elements for the test case, then sending clicks and type keys (such as
  pressing the "Enter" key) and then exits the browsers when done.
  Below is a view of the Selenium Webdriver architecture:

  .. figure:: ../image/se-webd-arch.png
     :width: 400px

     Selenium Webdriver architecture [#f1]_

  .. _selenium ide:

* **Selenium IDE (Integrated Development Environment)**: Also a component of the
  Selenium framework, the IDE is an browser add-on (Chrome and Firefox only)
  that allows for the recording and run/playback of test cases, allowing users
  to then export their recorded scenarios in a multitude of programming
  languages. The IDE provides a GUI that is ideal for  those with limited
  development knowledge or those trying to get save time on figuring our
  browsers variables to pull in their scripts. While we will mainly focus on
  Webdriver, it is handy to have IDE downloaded and added to the browser for
  later weeks. Below is a view of the Selenium IDE architecture:

  .. figure:: ../image/se-ide-arch.png
     :width: 400px

     Selenium IDE architecture [#f2]_

  .. _pytest:

* **PyTest**: A test automation framework that allows for the creation
  of simple and scalable test cases in WebDriver. It allows for the grouping and
  running of all tests (as opposed to one at a time) and tracks testing metrics
  such as number of tests passed or failed. With pyTest, test scripts are
  identified by having the word "test" in the script name and test cases are
  written as functions.While it is not necessary to use pyTest, having it makes
  test automation easy and efficient.


First Test Case
---------------

Since we are using pytest as our framework, we need to ensure that our test case
name is preceded with "*test*". The test case below will launch a Chrome browser
, access Google, then proceed to search for "Selenium", return results, and then
exit the browser.

.. literalinclude:: ../../tests/first_test.py
   :linenos:
   :caption: First Test Script

`See Code on GitHub <https://github.com/haybgq/cis385/blob/main/tests/first_test.py>`__


Breakdown of Time Spent
-----------------------

**Total Hours**: 12 hours

* **Monday, 1-10-2022**: 30 minutes
   * Met with Prof. Craven to discuss class/project expectations.

* **Thursday, 1-13-2022**: 30 minutes
   * Met with Prof. Craven to setup Sphinx and ReadMe.

* **Friday, 1-14-2022**: 1.5 hours
   * Setup documentation for About Page.

* **Monday, 1-17-2022**: 4 hours
   * Created Report 1: Getting Started page.
   * Pushed changes to github.

* **Wednesday, 1-19-2022**: 5.5 hours
   * Added additional notes to Getting Started page
   * Created and pushed first test script.
   * Updated ReadMe and Requirements files.
   * Met with Dr. Craven to discuss Report 1 and demo first test case.
   * Made updates to documentation following feedback from Dr. Craven.

References
----------

* `Code <https://github.com/haybgq/cis385>`_

.. rubric:: Footnotes:
.. [#f1] Bodke, A. (2020, May 7). Enhanced test automation with selenium
   WebDriver and pytest. Opcito. Retrieved January 19, 2022, from https://www.opcito.com/blogs/enhanced-test-automation-with-selenium-webdriver-and-pytest
.. [#f2] Hristovski, T. (2021, February 8). Advanced usage of selenium IDE for
   web automated testing. IWConnect. Retrieved January 19, 2022, from https://iwconnect.com/advanced-usage-of-selenium-ide-for-web-automated-testing/