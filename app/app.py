from flask import Flask, request, make_response, render_template
import socket

app = Flask(__name__)

USERS = {"manh": "1234"}


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", hostname=socket.gethostname())


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if USERS.get(username) == password:
            resp = make_response(render_template("welcome.html", username=username))
            resp.set_cookie("session", f"lab-{username}", httponly=True)
            return resp
        return render_template("login.html", error="Invalid username or password")
    return render_template("login.html", error=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
