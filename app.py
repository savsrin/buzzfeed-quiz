# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import return_instructor
from flask import redirect


# -- Initialization section --
app = Flask(__name__)




# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/results', methods=["GET", "POST"])
def results(): 
    if request.method == "POST":
        user_drink = request.form["favorite_drink"]
        user_food = request.form["favorite_food"]
        user_coding = request.form["coding_level"]
        print(user_coding)
        user_instructor = return_instructor(user_drink, user_food, user_coding)
        if user_instructor == "-1":
            return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        print(user_instructor)
        return render_template('results.html', 
                            user_drink=user_drink,
                            user_food=user_food, 
                            user_coding=user_coding,
                            user_instructor=user_instructor)
    else:
        return "Error"
