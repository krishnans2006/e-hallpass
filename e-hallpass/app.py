from flask import Flask, render_template, redirect, url_for, request, session, flash

from settings import SECRET_KEY, READY_PASSWORD, ADMIN_PASSWORD


app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=("GET", "POST"))
def login():
    if "user" in session:
        return redirect(url_for("index"))
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if username == "ready" and password == READY_PASSWORD:
            session["user"] = "ready"
            flash("Logged in as Ready!")
            return redirect(url_for("form"))
        elif username == "admin" and password == ADMIN_PASSWORD:
            session["user"] = "admin"
            flash("Logged in as Admin!")
            return redirect(url_for("form"))
        else:
            flash("Invalid credentials!")
            return redirect(url_for("login"))
    
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out!")
    return redirect(url_for("index"))


@app.route("/form")
def form():
    if "user" not in session:
        return redirect(url_for("login"))
    
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)
