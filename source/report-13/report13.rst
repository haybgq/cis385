**Author**: *Guy Sinarinzi-Hay*

**Posted**: *4/18/22*

.. _report 13-Uploads&Downloads:

Report 13: Selenium WebDriver - Uploads & Downloads
===================================================

This report covers activities performed between 4/15/22 - 4/18/22.

.. contents:: Contents:
   :depth: 3
   :local:

.. _overview13:

Overview
--------

Files contain contents that one entity requires from another, and as such, are
shared to via a web application in the form of an upload or download. It is
a near-guarantee that automation testers will, at some point in their careers,
encounter file upload and/or download scenarios. This section covers how to
automate upload and download functionality.

.. _upload-files:

Uploading Files
---------------

The process of sending a file from the local device to an application or
external system over the internet is referred to as **Uploading**.

.. _standard-upload:

Standard Upload
^^^^^^^^^^^^^^^

The upload functionality is usually initiated by users clicking on a file
selection button, selecting a file (or multiple files), and then clicking on an
upload button to transfer copies of the selected files to their destination.

Automating standard upload only requires knowing the directory from which files
will be selected, i.e.: the *file path*, and using the ``sendkeys()`` element
interaction command to relay that file as follows:

.. code-block:: Python

   # Standard upload command
   element_name.sendkeys("this/is-the-path-for/file.txt")


This can seen in the automation script below:

[insert test case]

.. _drag-and-drop-upload:

Drag-and-Drop Upload
^^^^^^^^^^^^^^^^^^^^

There might be instances where a web application has a feature that allows users
to select the file from their local system and drag it into the upload box. This
is becoming more and more common in modern day web applications, and with them,
the increasing need to automate the drag-and-drop functionality.

You may encounter one of two drag-and-drop scenarios:

* **Scenario 1:** User drags file from local system to web application. In this
  case, we use the ``sendkeys()`` function in a similar manner that we did in
  the :ref:`Standard Upload <standard-upload>` section.

  The automation script below demonstrates this example:

  [insert test case]

* **Scenario 2:** User can access their local directory in-app, but still needs
  to drag file into the upload box for a successful upload. This scenario is a
  little more complicated and requires the use of the ``drag_and_drop()``
  function, which is part of the ``ActionChains`` class.

  The Action Chains [#f1]_ are used to automate secondary interactions such as
  context menu, mouse button actions, key press and mouse movements (of which
  drag-and-drop is a feature). The following syntax is to import and create
  an Action Chains object.

  .. code-block:: Python

     # Import Action Chains
     from selenium.webdriver import ActionChains
     # Create an action chain object
     action = ActionChains(driver_object)

  From the Action Chains object, we can then use the ``drag_and_drop()`` [#f2]_
  function to hold down the left mouse button on the source element, and move it
  to the target element, then releases the mouse button. The following syntax is
  used to drag and drop elements:

  .. code-block:: Python

     # Drag-and-drop syntax
     drag_and_drop(source_element, target_element)

  The automation script below shows one element box being drag-and-dropped into
  another.

  [insert test case]

  **Note**: While this does not demonstrate an actual file being d
  ragged and dropped (we could not find a demo site with this specific scenario),
  the code and concept used is identical.

.. _download-files:

Downloading Files
-----------------

The process of retrieving a file from the an external source or application on
the internet to your local device is referred to as **Downloading**.

.. _standard-download:

Standard Download
^^^^^^^^^^^^^^^^^

Similar to the the :ref:`Standard Upload <standard-upload>` functionality, the
standard download consists of users finding a "Download" button that they click,
from which the event to download the file is then created. The main difference
between uploads and downloads in automation comes down to the file path. When
the download button is clicked, the file is automatically downloaded to the
default download folder for most browsers.

The automation script below shows a straight-forward standard download, where
merely clicking the download button is all that is required to pass the test:

[insert test case]

.. _specify-download-directory:

Specify Download Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^

There will be times where we want to store the downloaded files in a specified
location rather than the default directory. Such instances will require a few
configurations to be completed.

We begin by using the following syntax to import the ``ChromeOptions`` class
(note: if you are using a different browser, you will need to look into the
corresponding `Options <https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.chrome.options>`_
class) that is used to configure browser settings:

.. code-block:: Python

   # Import Chrome Options
   from selenium.webdriver.chrome.options import Options
   # Create a chrome object
   options = webdriver.ChromeOptions()

Then, we can set the download directory parameter as part of the browser
preferences:

.. code-block:: Python

   # Specify download directory
   preferences = ("download.default_directory": "file-path, "safebrowsing.enabled":"boolean")
   # Send preference to ChromeOptions object using experimental option method
   options.add_experimental_option("prefs", preferences)

Finally, we pass all the browser settings to the Webdriver object so they may
be included in every run instance:

.. code-block:: Python

   # Create a webdriver object
   # and pass the Chrome options with new download directory
   driver = webdriver.Chrome(chrome_options=options)

The automation script below shows an example where the file is downloaded to
a specified directory.

[insert test case]


Considerations
--------------

When automating upload and download functionality, we will want to address the
following:

1. **File Content Validation**: The last thing we want is to upload or download
   corrupted or infected files. Therefore, consider adding some validation
   libraries (at the time of this posting, Selenium does not have built-in file
   validation modules -- *should we build them one?*).

2. **Dialog Box Interaction**: When downloading files, certain browsers may
   show dialog boxes that prompt users to select a path for the file to be saved
   or how to open said file. Unfortunately, because those are technically
   OS-level dialog boxes, Selenium does not currently see them. Consider whether
   or not the business users have a use for them, and if they do not, then it
   might be easier to disable them so your automation scripts do not fail.
   The quickest way to disable these dialog boxes is through browser settings.
   However, there are third party libraries that could be imported to help
   disable them, or certain Selenium browser configuration settings that may
   work, but these may be `time-consuming <https://blog.j-labs.pl/2017/02/Selenium-Webdriver-browser-preferences-for-downloading-files>`_.

.. _time spent13:

Breakdown of Time Spent
-----------------------

**Total Hours**: **11.5 hours**

* **Friday, 4-15-2022**: 3 hours
   * Created Report 13 initial outline.
   * Researched upload and download automation process.

* **Saturday, 4-16-2022**: 2 hours
   * Added documentation for standard and drag-and-drop upload functionality.

* **Sunday, 4-17-2022**: 2 hours
   * Added documentation for standard and set location download functionality.

* **Monday, 4-18-2022**: 4.5 hours
   * Added test script for upload functionality.
   * Added test script for download functionality.
   * Pushed code to GitHub.
   * Reviewed report with Dr. Craven.

.. _references13:

References
----------

* `Link to test cases on GitHub <https://github.com/haybgq/cis385/tree/main/tests>`_

.. rubric:: Footnotes:
.. [#f1] Selenium. (2011). Selenium Action Chains.
   Retrieved April 17, 2022, from https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains
.. [#f2] Selenium. (2011). Selenium Action Chains Drag_and_Drop.
   Retrieved April 17, 2022, from https://selenium-python.readthedocs.io/api.html#selenium.webdriver.common.action_chains.ActionChains.drag_and_drop