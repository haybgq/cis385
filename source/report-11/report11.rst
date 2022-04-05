**Author**: *Guy Sinarinzi-Hay*

**Posted**: *4/3/22*

.. _report 11-UserLogin:

Report 11: Selenium WebDriver - User Login & 2FA
================================================

This report covers activities performed between 3/28/22 - 4/3/22. At some point
in your automation career, you will encounter web applications that require you
to log into an account, go through multi-factor authentication before
performing additional tasks on that account.


.. contents:: Contents:
   :depth: 3
   :local:

.. _overview11:

Overview
--------

At any given point in time, modern day users of any technology have been
required to log into a secured account to access private data. Examples include
logging into an account to check emails, accessing bank accounts online,
logging into the college website to see whether your favorite Computer Science
professor has given you a good grade for your flawless homework -- and the list
goes on. In order to login, a user must be authenticated using any one of the
following authentication factors:

.. _knowledge:

* **Knowledge Factors**: *Something you know.* Authorized users provide
  information only they know, such as passwords, personal identification numbers,
  or answers to challenge questions.

.. _possession:

* **Possession Factors**: *Something you have.* Essentially a key to a security
  lock, these are physical items possessed by authorized users, such as one-time
  passwords (OTP) sent to devices or security keys such as YubiKeys.

.. _inherence:

* **Inherence Factors**: *Something you are.* These consist of metrics that are
  integral and unique to authorized users. Examples include retina scanners,
  voice recognition or fingerprint readers.


With this in mind, we can then define factor authentication based on how many
factors are used as follows:

1. **Single-Factor Authentication (SFA)**: Known best as the most common form of
   authentication, SFA is a security control that relies on just one
   authentication factor. The most popular form of SFA is providing a password
   for a given username.

2. **Two-Factor Authentication (2FA/TFA)**: Also known as dual-factor
   authentication or two-step verification, 2FA uses two of the factors to
   verify a user's identity. The most common 2FA methods consist of one-time
   passwords sent via SMS or an authentication application such as Google
   Authenticator.

3. **Multi-Factor Authentication (MFA)**: Although 2FA is a type of MFA, which
   is why you may, from time to time, hear the terms interchanged, MFA could
   involve all three factors to authenticate users.

In this section, we will be covering how to automate single-factor and
two-factor authentication. For demo purposes, we will create our own login
page using flask and bootstrap, as shown below:

.. literalinclude:: ../../otp/app.py
   :linenos:
   :caption: Login Page [#f1]_

Make sure you have the flask server running before running any automation tests
against this login page.

.. _sfa login:

Single-Factor Authentication
----------------------------

If you have been following along from previous sections, then single-factor
login is a straight-forward process: All we need are the right locator elements
to find the username and password form fields. Then, we can use an interaction
command to enter the pertinent data and proceed to authenticate the user.
For a refresher on locators and interaction commands, please visit the
:ref:`Browser & Elements <report 4-Browser & Elements>` section.

The test script below shows a single-factor login scenario:

.. literalinclude:: ../../tests/test_login_single_factor.py
   :linenos:
   :emphasize-lines: 40-47
   :caption: Single-Factor Authentication

.. _tfa login:

Two-Factor Authentication
-------------------------

The two-step verification process requires a little more work from an automation
perspective. While the first step simply requires a username and password, the
second step often consists of using :ref:`possession factors <possession>` to
authenticate the user. As we do not have a YubiKey (hard tokens) to demonstrate
how that may work, we shall use a more common method involving one-time
passwords (OTPs) via soft tokens (mobile devices or applications).

.. _otp:

Understanding OTP
^^^^^^^^^^^^^^^^^

A One-Time Password is a string of digits, also known as the *authentication code*,
that can only be used once. This type of password is also referred to as a
*dynamic password* because it constantly changes, whereas traditional passwords
are known as *static passwords*.

OTPs are derived from secret keys that are used to run an algorithm and provide
a corresponding authentication code to the user. These secret keys, when
generated (usually during user registration), are stored both on the server and
the user's personal device (usually acquired via a `QR Code <https://www.hypr.com/qr-code-quick-response-code/>`_
or an alphanumeric string that is stored in an authenticator application). Once
the key is stored, it will be used to generate an authentication code that the
user will input into the application, which sends the value to the server for
comparison, and if the authentication code matches on the sever side, the user
passes verification.

OTPs that change after a set period are known as Time-Based One-Time Passwords
(TOTP). Authentication applications such as Google, Microsoft or Authy
authenticators generate TOTPs every 30 seconds. OTPs that are sent via email or
SMS are known as HMAC-Based One-Time Passwords (HOTP).

For automation purposes, we are only going to focus on TOTPs. For additional
literature on MFA standards, please refer to `RFC 4226 <https://datatracker.ietf.org/doc/html/rfc4226>`_ (HOTP)
and `RFC 6238 <https://datatracker.ietf.org/doc/html/rfc6238>`_ (TOTP).

.. _totp:

TOTP in Automation
^^^^^^^^^^^^^^^^^^

To automate 2FA, we need to be able to generate and verify TOTPs. The PyOTP
library can be used to serve this purpose. We begin by importing the ``pyotp``
library:

.. code-block:: Python

   import pyotp

The following methods are used with PyOTP:

.. csv-table:: PyOTP Methods [#f2]_
   :file: ../files/se-webd-pyotp.csv
   :widths: 25 75
   :header-rows: 1

Examples of these commands in use:

.. literalinclude:: ../../tests/otp_tests.py
   :linenos:
   :caption: PyOTP Examples

Now that we have a way to generate TOTPs, we can write an automation script that
provides the username and password on the login page, gets redirected to the
2FA page, where it fetches the security key and uses it to generate a TOTP, then
submits the information for authentication. When the user is authenticated, they
are redirected to the *Successful Login* page.

.. literalinclude:: ../../tests/test_login_two_factor.py
   :linenos:
   :emphasize-lines: 56-66
   :caption: Two-Factor Authentication


.. _considerations:

Considerations
--------------

As a test engineer, you will no doubt be required to automate user login flows
from time to time. When doing so, it is best to err on the side of caution by
considering the following:

1. **Consult with the Cybersecurity Department**: Depending on how or where your
   test cases are stored, some individuals may be able to access them. If your
   tests contain login credentials, this may open the door for malicious actors.

2. **Use a Secrets Manager**: Where applicable, it is best to use a secrets
   manager that requires the code to make calls to the storage system and
   retrieve login credentials. The credentials are not visible anywhere in the
   code, and passwords and OTP tokens alike are changed and rotated to prevent
   likelihood of a breach.

3. **The More Authentication Factors Used, The Better**: While TFA is the
   accepted standard, always consider adding more factors to minimize chances
   of a successful identity theft. While adding more factors might also mean
   verification is time consuming, the trade-off is incomparable where identity
   and personal information is concerned.

.. _time spent11:

Breakdown of Time Spent
-----------------------

**Total Hours**: **17 hours**

* **Monday, 3-28-2022**: 2 hours
   * Created Report 11
   * Researched user login automation

* **Tuesday, 3-29-2022**: 4 hours
   * Added Overview documentation
   * Created initial login page route

* **Wednesday, 3-30-2022**: 3.5 hours
   * Completed documentation for Overview
   * Added documentation for Single-Factor Authentication
   * Added form control code for login page route
   * Added test case for single-factor login

* **Thursday, 3-31-2022**: 2.5 hours
   * Added documentation Two-Factor Authentication
   * Added 2FA page and form control

* **Saturday, 4-1-2022**: 3 hours
   * Added OTP and TOTP documentation
   * Created test case for 2FA Login

* **Sunday, 4-3-2022**: 1.5 hours
   * Added documentation for PyOTP
   * Revised 2FA Login script
   * Pushed code to GitHub

* **Thursday, 4-5-2022**: 0.5 hours
   * Made revisions based on feedback from Dr. Craven
   * Pushed revisions to GitHub

.. _references10:

References
----------

* `Link to test cases on GitHub <https://github.com/haybgq/cis385/tree/main/tests>`_

.. rubric:: Footnotes:
.. [#f1] Joel, P. (2021, April 27). Implementing TOTP 2FA in Python and Flask.
   Section. Retrieved April 1, 2022, from https://www.section.io/engineering-education/implementing-totp-2fa-using-flask/
.. [#f2] Python Package Index. (2021, February 21). PyOTP. PyPI. Retrieved April 3, 2022, from https://pypi.org/project/pyotp/