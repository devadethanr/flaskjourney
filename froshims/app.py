from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = ["Basketball", "Soccer", "Frisbee", "Rugby"]
@app.route('/')
def index():
    return render_template("index.html", sports = SPORTS)

@app.route("/register", methods = ["POST"])
def register():
    # if not request.form.get("name") or not request.form.get("sport"):
        # return "failure"
    if not request.form.get("name"):  #or request.form.get("sport") not in SPORTS
        return render_template("failure.html")
    for sport in request.form.getlist("sport"):
        if sport not in SPORTS:
            return render_template("failure.html")
    return render_template("success.html")

# https://youtu.be/-aqUek49iL8?si=EhNGo3NdbS2Yk0YJ&t=4649 1:17:29