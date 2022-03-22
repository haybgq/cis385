**Author**: *Guy Sinarinzi-Hay*

**Posted**: *3/21/22*

Report 10: Selenium WebDriver - Exception Handling
==================================================

This report covers activities performed between 3/14/22 - 3/21/22. As testers,
we are bound to encounter errors or exceptions in any given test cycle. Graceful
exception handling ensures that a test flow continues while acknowledging that
there is an issue.

.. contents:: Contents:
   :depth: 3
   :local:

.. _overview10:

Overview
--------

In Selenium WebDriver, exceptions are errors that are generated when an
unexpected event occurs, and serve as the basis of troubleshooting. When an
exception is raised, the user flow comes to a halt (crash), along with a string
of errors or messages -- known as tracebacks -- to help users determine the root
cause.

Exception handling serves to prevent test runs from crashing by catching the
exception, and providing directives to resolve or report it. Examples of this
can be found in the :ref:`Exception Handling Methods <exception handling methods>`
section.

.. _exception types:

Types of Exceptions
-------------------

We have encountered certain Selenium exceptions in previous chapters, such as
``NoSuchElementException`` (:ref:`Implicit Waits <implicit wait>`),
``AssertionError`` (:ref:`Soft Assertions <soft assertions>`) and
``TimeoutException`` (:ref:`Explicit Waits <explicit wait>`). The full list of
Selenium-specific exceptions can be seen below:

.. csv-table:: Selenium Common Exceptions [#f1]_
   :file: ../files/se-webd-common-exceptions.csv
   :widths: auto
   :header-rows: 1

**Note**: The ``AssertionError`` will not be seen in the above list because
this exception is not unique to Selenium. Rather, it is inherited from the
Exception class that is native to Python and can thus be used without importing
a package. For more information on ``AssertionError``, please visit :ref:`Soft Assertions <soft assertions>`.

.. _exception handling methods:

Exception Handling Methods
--------------------------

The first step of Selenium Python exception handling requires us to import the
package that contains all Selenium exception classes. The syntax below is used
for the import:

.. code-block:: Python

   from selenium.common.exceptions import NameOfException

Then, we use the ``try-except`` block to handle exceptions in the various ways
outlined below:

.. _single exception handling:

Single Exception Handling
^^^^^^^^^^^^^^^^^^^^^^^^^

If we are handling only one exception, we can use the following syntax:

.. code-block:: Python

   try:
        "block of code to test for errors."
   except NameOfException:
        "block of code to handle the error."

This can be seen in the example below, where we have added logic to handle the
exception generated when an element is not found:

.. literalinclude:: ../../tests/test_single_exception_handling.py
   :linenos:
   :emphasize-lines: 6, 16-27
   :caption: Single Exception Handling

.. _multiple exception handling:

Multiple Exceptions Handling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When handling multiple exceptions, the following syntax is used:

.. code-block:: Python

   try:
        "block of code to test for errors."
   except NameOfExceptionOne:
        "block of code to handle the first type error."
   except NameOfExceptionTwo:
        "block of code to handle the second type of error."

We can define as many ``except`` blocks as we need, bearing in mind that only
one block will be executed if an error occurs, i.e.: if more than one exception
is raised during the execution flow, only the first exception will be handled
and the flow will continue. This is demonstrated in the test below, where we
handle both an ``AssertionError`` and a ``NoSuchElementException``:


.. literalinclude:: ../../tests/test_multiple_exceptions_handling.py
   :linenos:
   :emphasize-lines: 31-36, 38-40
   :caption: Multiple Exceptions Handling

In this example, despite both exceptions being raised, only the ``NoSuchElementException``
block will be executed due the that exception being raised before ``AssertionError``.

.. _best practices:

Best Practices
--------------

1. **Use exception and error handling only when necessary**: Catching errors or
   exceptions slows down code and impacts performance.

2. **Handle the exceptions you expect**: Specify errors that you expect will
   occur and refrain from using *catch-all* ``except`` clauses, denoted by the
   highlighted syntax:

  .. code-block:: Python
     :emphasize-lines: 7-8

     try:
          "block of code to test for errors."
     except NameOfExceptionOne:
          "block of code to handle the first type error."
     except NameOfExceptionTwo:
          "block of code to handle the second type of error."
     except:
          "block of code to handle all other exceptions"

  Severe exceptions can be missed when using the *broad except block*, which
  could, in turn, result in bad tests and impact overall quality. Therefore, to
  reiterate, please handle the exceptions you expected, and not the unknowns.

.. _time spent10:

Breakdown of Time Spent
-----------------------

**Total Hours**: **12.5 hours**

* **Tuesday, 3-14-2022**: 1 hour
   * Created Report 10
   * Added Overview documentation

* **Tuesday, 3-15-2022**: 2 hours
   * Researched types of exceptions
   * Added initial documentation for types of exceptions

* **Wednesday, 3-16-2022**: 4 hours
   * Completed documentation for Types of Exceptions
   * Added documentation and test cases for Exception Handling Methods

* **Thursday, 3-17-2022**: 2.5 hours
   * Added single exception handling documentation and tests

* **Monday, 3-21-2022**: 3 hours
   * Added multiple exceptions handling documentation, test case and best
     practices

.. _references10:

References
----------

* `Link to test cases on GitHub <https://github.com/haybgq/cis385/tree/main/tests>`_
* `Link to Exceptions documentation <https://selenium-python.readthedocs.io/api.html#module-selenium.common.exceptions>`_

.. rubric:: Footnotes:
.. [#f1] Selenium. (2011). Selenium WebDriver Common Exceptions.
   Retrieved March 16, 2022, from `Selenium Common Exceptions <https://www.selenium.dev/selenium/docs/api/py/common/selenium.common.exceptions.html>`_