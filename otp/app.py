# Demo Page

# Import required libraries
from flask import *
from flask_bootstrap import Bootstrap
import pyotp

# Configure Flask application
app = Flask(__name__)
app.config["SECRET_KEY"] = "APP_SECRET_KEY"
Bootstrap(app)


# Homepage route
@app.route("/")
def index():
    return render_template("home.html")


# Login Page route
@app.route("/login/")
def login():
    return render_template("login.html")


# Login Form route
@app.route("/login/", methods=["POST"])
def login_form():
    # Login Credentials
    creds = {"username": "thatProfessor", "password": "isCraven"}

    # Get form data
    username = request.form.get("username")
    password = request.form.get("password")

    # Authenticate User-Entered Credentials against Login Credentials
    if username == creds["username"] and password == creds["password"]:
        # Notify users that credentials are valid
        flash("Your credentials are valid!", "success")
        return redirect(url_for("login_2fa"))
    else:
        # Notify users that login credentials are not valid
        flash("You have supplied invalid login credentials! Please try again!",
              "danger")
        return redirect(url_for("login"))


# 2FA Page route
@app.route("/login/2fa/")
def login_2fa():
    # generating random secret key for authentication
    secret = pyotp.random_base32()
    return render_template("login_2fa.html", secret=secret)


# 2FA Form route
@app.route("/login/2fa/", methods=["POST"])
def login_2fa_form():
    # getting secret key used by user
    secret = request.form.get("secret")

    # verifying user-provided OTP with PyOTP
    if pyotp.TOTP(secret).verify(request.form.get("otp")):
        # inform users if OTP is valid
        flash("The TOTP token is valid!", "success")
        return redirect(url_for("login_successful"))
    else:
        # inform user if OTP is invalid
        flash("You have supplied an invalid 2FA token!", "danger")
        return redirect(url_for("login_2fa"))


# Success Page route
@app.route("/login_successful/")
def login_successful():
    return render_template("login_successful.html")


# Run Flask Server
if __name__ == "__main__":
    app.run(debug=True)
