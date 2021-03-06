Selenium - UI Automation with Python
====================================

This project will consist of automating a user flow for a web/browser-based
interface via the exploration and use of Selenium Tools, namely: Selenium
WebDriver and Selenium IDE.

Selenium WebDriver Setup
------------------------

1. Import all packages in `requirements.txt <https://github.com/haybgq/cis385/blob/main/requirements.txt>`_
   as follows:

   .. code-block:: Shell

      # Install all requirements
      # Note: Will not work on pinned (versioned) packages
      pip install -r requirements.txt

      # If you think you are missing only certain packages
      pip install --ignore-installed -r requirements.txt

      # To upgrade current requirements
      pip install --upgrade -r requirements.txt


2. If there are any errors, ensure that you have the latest pip version as
   follows:

   .. code-block:: Shell

      # Check pip version
      > pip --version

      # Install pip version
      > pip install

      # Upgrade Pip
       > pip install --upgrade pip

3. If packages are not imported, manually install them as follows:

   .. code-block:: Shell

      # Selenium:
      > pip install selenium

      # Pytest:
      > pip install pytest

      # WebDriver Manager:
      > pip install webdriver-manager

4. Install Drivers:
   https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

Selenium IDE Setup
------------------

1. Launch your Chrome, Edge and/or Firefox browser.

2. Navigate to the Selenium IDE `website <https://www.selenium.dev/selenium-ide/>`_
   and install the appropriate extension to your browser:

   * `Chrome <https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd>`_

   * `Edge <https://microsoftedge.microsoft.com/addons/detail/selenium-ide/ajdpfmkffanmkhejnopjppegokpogffp>`_

   * `Firefox <https://addons.mozilla.org/en-GB/firefox/addon/selenium-ide/>`_

     * **Note**: At the time of this post, the Firefox extension is undergoing
       some changes and is thus not available via the link. For alternative
       methods, please see `GitHub issue #1309 <https://github.com/SeleniumHQ/selenium-ide/issues/1309>`_.

3. Click on the new Extension and confirm Selenium IDE GUI launches.

Selenium IDE Command-Line Runner
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Install NodeJS and Node Package Manager (npm) from your terminal/command prompt:

  * For MacOS users:

    .. code-block:: Shell

       #package manager is usually installed with node
       > brew install node

  * For Other users:

    * `NodeJS <https://nodejs.org/en/download/>`_
    * `Node Package Manager <https://nodejs.org/en/download/package-manager/>`_

2. Use Node Package Manger to install ``selenium-side-runner``:

   .. code-block:: Shell

      > npm install -g selenium-side-runner

3. Install appropriate browser drivers:

   .. code-block:: Shell

      # Chrome:
      > npm install -g chromedriver

      # Edge:
      > npm install -g edgedriver

      # Firefox:
      > npm install -g geckodriver

      # Internet Explorer:
      > npm install -g iedriver

     #Safari driver is already pre-installed on MacBooks.
