from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Add your login logic here

        return redirect("/dashboard")  # Redirect to the dashboard page after successful login

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        first_name = request.form["first_name"]
        surname = request.form["surname"]
        username = request.form["username"]
        password = request.form["password"]
        # Add your signup logic here

        return redirect("/login")  # Redirect to the login page after successful signup

    return render_template("signup.html")


@app.route("/dashboard")
def dashboard():
    # Add your dashboard logic here
    return "Dashboard Page"


if __name__ == "__main__":
    app.run(debug=True)
