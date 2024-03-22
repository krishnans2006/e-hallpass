from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return "Login"


if __name__ == "__main__":
    app.run(debug=True)
