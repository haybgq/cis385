**Author**: *Guy Sinarinzi-Hay*

**Posted**: *3/4/22*

.. _report-8:

Report 8: Selenium WebDriver - Assertions
=========================================

This report covers activities performed between 2/21/22 - 3/4/22. As we return
to Selenium WebDriver features, we explore the value of Assertions in test
automation.

.. contents:: Contents:
   :depth: 3
   :local:

.. _overview8:

Overview
--------

.. figure:: ../image/se-webd-assertive-bn-rude.gif
   :width: 400px

   Can We Pull It Off?

The verb *Assert* means to state a fact or belief confidently and forcefully. [#f1]_
In test automation, Asserts, also known as *Assertions*, are used to set the
expectation under which a test case passes or fails validation. The following
syntax is used to denote assertions:

.. code-block:: Python

   assert condition, "message"

The parameters passed into the assert expression are defined as follows:

* **Condition** (required): The expectation that will be tested against.
* **Message** (optional): The message to be displayed should the assertion fail.

When a test case passes, the report generated at the end of an execution will
not look much different than it would had there not been an assert in the script.
However, when the test fails on assert, a report will be generated showing the
expected (*asserted*) value and the actual (*current*) value.

.. _assertion types:

Types of Assertions
-------------------

Assertions can be broken down into two categories: Hard and Soft Assertions.

.. _hard assertions:

Hard Assertions
^^^^^^^^^^^^^^^

A hard assertion results in the test execution being aborted when the assertion
condition is not met, i.e.: returns false. When this happens, an ``AssertionError``
is thrown and the test case fails. This type of assertion is to be used
when it serves no purpose to continue a test if the expected condition is not
met.

In the test script below, we have a scenario where we navigate to the Python
website, print the link (*url*) that was used, then print a statement noting that
we have landed on the Python homepage, and enter "*asserts*" in the search box:

.. literalinclude:: ../../tests/test_without_assertion.py
   :linenos:
   :caption: Test Without Assertions

This particular test has no assertions, and when ran, will, in fact, pass
without error:

.. code-block::

   ============================= test session starts ===========================
   collecting ... collected 1 item
   test_without_assertion.py::TestWithoutAssertions::test_navigate_to_page
   ============================= 1 passed in 4.54s =============================

   Process finished with exit code 0
   PASSED          [100%]
   Link Used = https://www.python.org/
   Python Org homepage has been reached!

The issue arises when we replace Python's link with Google's, as follows:

.. code-block:: Python

   # Replace Python link with Google link
   url = "https://www.google.com/"

Then, run the test again. Where this test should fail, it unfortunately passes,
as seen below:

.. code-block::

   ============================= test session starts ===========================
   collecting ... collected 1 item
   test_without_assertion.py::TestWithoutAssertions::test_navigate_to_page
   ============================= 1 passed in 4.90s =============================

   Process finished with exit code 0
   PASSED          [100%]
   Link Used = https://www.google.com/
   Python Org homepage has been reached!

This is as an example of a bad test case that passes where it should fail.
Really, it is not a bad test case so much as it is a bad QA Engineer that did
not set the correct expectations.

To rectify the situation, we will add the following assertions:

.. literalinclude:: ../../tests/test_assertions.py
   :emphasize-lines: 28-29, 41
   :linenos:
   :caption: Test Assertions

* **Line 28-29**: The assertion checks whether the current page title matches
  the expected page title, i.e.: *Welcome to Python.org*. Should they not match,
  the assertion returns a message stating that the current homepage is not what
  was expected.

* **Line 41**: The assertion checks whether the current search string we entered
  into the search box matches the string we expected, i.e.: *"asserts"*.

In order to test that our assertion works, we will run a test against the Google
link we used earlier. The results are seen below:

.. code-block:: Text

   ============================= test session starts ===========================
   collecting ... collected 1 item
   test_assertions.py::TestAssertions::test_assert_scenario
   ============================= 1 passed in 4.90s =============================

   Process finished with exit code 0
   FAILED          [100%]
   Link Used = https://www.google.com/
   Expected :'Welcome to Python.org'
   Actual   :'Google'
   E       AssertionError:
   E         Google is not Python's homepage! Check your link again.
   E       assert 'Google' == 'Welcome to Python.org'
   E         - Welcome to Python.org
   E         + Google

The above results indicate that an ``AssertionError`` was thrown, where the
expect title for Python did not match the actual title for Google. We also see
a message showing that *Google is not Python's homepage*.

Having seen that our assertion works when the link is not what we expected, we
would also test that when the expected link is provided, no errors are thrown.
After changing the link back to Python organization, we ran the test, and it
passed as expected.

.. code-block::

   ============================= test session starts ===========================
   collecting ... collected 1 item
   test_assertions.py::TestAssertions::test_assert_scenario
   ============================= 1 passed in 3.51s =============================

   Process finished with exit code 0
   PASSED          [100%]
   Link Used = https://www.python.org/
   Python Org homepage has been reached!

With this, we can confirm that our assertions function as desired.

.. _soft assertions:

Soft Assertions
^^^^^^^^^^^^^^^

Soft Assertions, when encountered in the test execution, will not hinder the
execution from completing. Rather, they will notify the tester than something is
wrong, and let the test execution run until completion. While certain test
frameworks, such as `unittest <https://chercher.tech/python/assertion-unittest-python-selenium>`_
or `jUnit <https://www.browserstack.com/guide/verify-and-assert-in-selenium>`_,
have extensive libraries to use for soft assertion classes, in pyTest, we use
exception handling to allow the execution to keep running despite throwing an
``AssertionError``. Soft Assertions are used in cases where we may want to see
what other parts of the code have errors, without having to stop at every error
encountered.

The following exception handling syntax is used for a soft assertion:

.. code-block:: Python

   try:
        assert condition, "message"
   except AssertionError:
        handle the error

To test the soft assertion, we will add it to the script below, where we expect
a Python homepage title, but instead receive Google's title:

.. literalinclude:: ../../tests/test_soft_assertions.py
   :emphasize-lines: 29-35
   :linenos:
   :caption: Test Soft Assertions


When the test is executed, we can see that it was executed to completion, with a
final result showing as passed:

.. code-block::

   ============================= test session starts ===========================
   collecting ... collected 1 item
   test_soft_assertions.py::TestSoftAssertions::test_soft_assert_scenario
   ============================= 1 passed in 4.25s =============================

   Process finished with exit code 0
   PASSED          [100%]
   Link Used = https://www.google.com/
   Assertion failed. Google is not Python's homepage! Check your link again.
   Python Org homepage has been reached!

Notice that an ``AssertionError`` was thrown during test execution, however, the
try exception block handled it by reporting an error without halting the test
execution.

.. _time spent8:

Breakdown of Time Spent
-----------------------

**Total Hours**: **11 hours**

* **Monday, 2-28-2022**: 2.5 hours
   * Setup initial documentation for Report 8.
   * Began research on types of assertions.

* **Tuesday, 3-1-2022**: 1.5 hours
   * Added documentation for hard asserts.

* **Wednesday, 3-2-2022**: 3 hours
   * Created test scripts with hard asserts.

* **Thursday, 3-3-2022**: 1.5 hours
   * Added documentation for soft asserts.
   * Created test script with soft assert.

* **Friday, 3-4-2022**: 2.5 hours
   * Added finishing touches to Report 8 documentation.
   * Demoed work to Dr. Craven.
   * Made updates based on feedback from Dr. Craven.
   * Pushed all changes to GitHub.


.. _references8:

References
----------

* `Link to test cases on GitHub <https://github.com/haybgq/cis385/tree/main/tests>`_

.. rubric:: Footnotes:
.. [#f1] Lexico Dictionaries. (n.d.). Assert English definition and meaning.
   Lexico Dictionaries | English. Retrieved March 4, 2022, from https://www.lexico.com/en/definition/assert