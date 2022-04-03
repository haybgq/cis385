import pyotp


def tfa_validator():
    totp = pyotp.TOTP("VNB4JYKRDDHJTEFO3YZ7ELIKRH3W4X6N")  # Secret Token
    print("Auth Code = ", totp.now())


# TFA Validator
tfa_validator()
