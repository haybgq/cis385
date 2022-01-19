Report 1: Getting Started
=========================

This report covers activities performed between 1/10/22 - 1/19/22. There was a
slight delay in delivering it due to unforeseen circumstances already discussed
with Prof. Craven.

Setup
-----

To get started, access the ``readme.rst`` file in the `GitHub
repository <https://www.selenium.dev/>`_ and follow the steps outlined in the
document.

By the end of the installation, we should have:
1. Selenium installed.
2. pyTest installed.
3. The correct most up to date browser webdriver installed.

In order to create and execute successful automation tests, we will download and
configure the tools below:

* **Selenium Webdriver**: A core component of the overall Selenium framework,
  it is an open-source tool that allows for the automation of user-facing web
  applications such as Linux, Mac and Windows. As a collection of open-source
  APIs Selenium WebDriver performs web testing across browsers such as Chrome,
  Safari, Edge, etc. WebDriver works by opening a browser, identifying
  browser elements for the test case, then sending clicks and type keys (such as
  pressing the "Enter" key) and then exits the browsers when done.
  Below is a view of the Selenium Webdriver architecture:

  .. image:: image/se-webd-arch.png
    :width: 400
    :alt: Selenium Webdriver architecture


* **Selenium IDE (Integrated Development Environment)**: Also a component of the
  Selenium framework, the IDE is an browser add-on (Chrome and Firefox only)
  that allows for the recording and run/playback of test cases, allowing users
  to then export their recorded scenarios in a multitude of programming
  languages. The IDE provides a GUI that is ideal for  those with limited
  development knowledge or those trying to get save time on figuring our
  browsers variables to pull in their scripts. While we will mainly focus on
  Webdriver, it is handy to have IDE downloaded and added to the browser for
  later weeks. Below is a view of the Selenium IDE architecture:

  .. image:: image/se-ide-arch.png
    :width: 400
    :alt: Selenium IDE architecture


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
name is preceded with "*test*". The test case below will launch a Chrome browser,
access Google, then proceed to search for "Selenium", return results, and then
close.

Access the test case on `GitHub
<https://github.com/haybgq/cis385/blob/main/tests/first_test.py>`_ .


Breakdown of Time Spent
-----------------------
* **Monday, 1/10**: 30 minutes
   * Met with Prof. Craven to discuss class/project expectations.

* **Thursday, 1/13**: 30 minutes
   * Met with Prof. Craven to setup Sphinx and ReadMe

* **Friday, 1/14**: 1.5 hours
   * Setup documentation for About Page

* **Monday, 1/17**: 4 hours
   * Created Report 1: Getting Started page
   * Pushed changes to github

* **Wednesday, 1/17**: 3.5 hours
   * Added additional notes to Getting Started page
   * Created and pushed first test script
   * Updated ReadMe and Requirements files
   * Met with Prof. Craven to discuss Report 1 and demo first test case