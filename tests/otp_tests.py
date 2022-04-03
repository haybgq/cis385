# PyOTP Examples

import pyotp


# Generate a Base 32 and Hex Security Key
def generate_security_key():
    print("random_base32 = ", pyotp.random_base32())
    print("random_hex = ", pyotp.random_hex())


# Generate a TOTP Code
def tfa_validator():
    totp = pyotp.TOTP("7D2P2IYDOKUK4YAH4YHT2T2WYJZVUIOB")
    print("Auth Code = ", totp.now())


generate_security_key()
tfa_validator()
