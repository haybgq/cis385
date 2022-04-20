**Author**: *Guy Sinarinzi-Hay*

**Posted**: *4/18/22*

(**Updated**: *4/19/22*)

.. _report 13:

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
shared via a web application in the form of an upload or download. It is
a near-guarantee that automation testers will, at some point, encounter file
upload and/or download scenarios. This section covers how to automate upload and
download functionality.

.. _upload-files:

Uploading Files
---------------

The process of sending a file from the local device to an application or
external system over the internet is referred to as **Uploading**.

The upload functionality is initiated by users clicking on a file selection
button, selecting a file (or multiple files), and then clicking on an
upload button to transfer copies of the selected files to the appropriate
destination.

Automating upload scenarios requires knowing the directory from which files
will be selected, i.e.: the *file path*, and the file name. The ``sendkeys()``
element interaction command is used to relay the file for upload as follows:

.. code-block:: Python

   # Standard upload command
   element_name.sendkeys("this/is-the-path-for/file.txt")


The automation script below shows a local directory being accessed, after which
it us uploaded to the application:

.. literalinclude:: ../../tests/test_standard_upload.py
   :linenos:
   :emphasize-lines: 29-39
   :caption: Test Upload

**Note**: While some applications contain a drag and drop upload feature,
at the time of this post, Selenium WebDriver does not possess a way to drag and
drop files from the operating system (OS) to a web-application. However,
Selenium does possess the ability to drag and drop elements in an application.

.. _download-files:

Downloading Files
-----------------

The process of retrieving a file from an external source or application on
the internet and storing it on the local device is referred to as **Downloading**.

.. _standard-download:

Standard Download
^^^^^^^^^^^^^^^^^

Similar to the :ref:`Upload <upload-files>` functionality, the standard download
entails users finding a "Download" button that they can click, from which the
event to download the file is then triggered. The main difference
between uploads and downloads in automation comes down is based on the role that
file paths play for both features. When the download button is clicked, the file
is automatically downloaded to a default *Downloads* folder for most browsers.

The automation script below shows a standard download scenario where the
download link is clicked, then validation is added to confirm that the file was
downloaded to the default *Downloads* folder successfully before being deleted:

.. literalinclude:: ../../tests/test_standard_download.py
   :linenos:
   :emphasize-lines: 46-74
   :caption: Test Standard Download

.. _specify-download-directory:

Specify Download Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^

There will be times when we want to store the downloaded files in a specified
location, rather than the default directory. Such instances will require a few
configurations to be completed before files are stored in a different directory.

We begin by using the following syntax to import the ``ChromeOptions`` class
that is used to configure browser settings.

**Note:** If you are using a different browser, you will need to look into the
corresponding `Options <https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.chrome.options>`_
class that works for your browser.

.. code-block:: Python

   # Import Chrome Options
   from selenium.webdriver.chrome.options import Options
   # Create a chrome options object
   options = webdriver.ChromeOptions()

Then, we can set the download directory parameter as part of the browser
preferences:

.. code-block:: Python

   # Specify download directory
   preferences = {"download.default_directory": "file-path"}
   # Send preference to ChromeOptions object using experimental option method
   options.add_experimental_option("prefs", preferences)

Finally, we pass all the browser settings to the Webdriver object so they may
be included in every session ran:

.. code-block:: Python

   # Create a webdriver object
   # and pass the Chrome options with new download directory
   driver = webdriver.Chrome(chrome_options=options)

The automation script below shows an example where the file is downloaded to
a specified directory.

.. literalinclude:: ../../tests/test_download_specified_location.py
   :linenos:
   :emphasize-lines: 4, 18-27, 61-72
   :caption: Test Downloading in Specified Location


Considerations
--------------

When automating upload and download functionality, we will want to address the
following:

1. **File Content Validation**: The last thing we want is to upload or download
   corrupted, empty or infected files. Therefore, consider adding some validation
   libraries (at the time of this posting, Selenium does not have built-in file
   Input-Output (IO) validation modules -- *should we build them one?*)
   to help with this.

2. **Dialog Box Interaction**: When downloading files, certain browsers may
   show dialog boxes that prompt users to select a path for the file to be saved
   or how to open the saved file. Unfortunately, because those are technically
   OS-level dialog boxes, Selenium does not currently *see* them and can thus
   not interact with these boxes. Consider whether or not the business users
   have a need for these dialog boxes, and if they do not, then it
   might be easier to disable them so your automation scripts do not fail.
   The quickest way to disable these dialog boxes is through browser settings.
   However, there are third party libraries that could be imported to help
   disable them, or certain Selenium browser configuration settings that may
   work, but these may be `time-consuming <https://blog.j-labs.pl/2017/02/Selenium-Webdriver-browser-preferences-for-downloading-files>`_
   as they would require configuring every automation workstation available.

.. _time spent13:

Breakdown of Time Spent
-----------------------

**Total Hours**: **15 hours**

* **Friday, 4-15-2022**: 3 hours
   * Created Report 13 initial outline.
   * Researched upload and download automation process.

* **Saturday, 4-16-2022**: 2 hours
   * Added documentation for standard and drag-and-drop upload functionality.

* **Sunday, 4-17-2022**: 2 hours
   * Added documentation for standard and set location download functionality.

* **Monday, 4-18-2022**: 7.75 hours
   * Added test script for upload functionality.
   * Added test script for download functionality.
   * Pushed code to GitHub.
   * Reviewed report with Dr. Craven.
   * Made revisions based on Dr. Craven's feedback.

* **Tuesday, 4-19-2022**: 0.25 hours
   * Pushed revised code to GitHub.

.. _references13:

References
----------

* `Link to test cases on GitHub <https://github.com/haybgq/cis385/tree/main/tests>`_
