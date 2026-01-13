from flask import Flask, render_template, request, jsonify
import os
import joblib
import numpy as np

app = Flask(__name__)

# ---------------- PATHS ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ML_DIR = os.path.join(BASE_DIR, "ml")

goal_model = joblib.load(os.path.join(ML_DIR, "goal_model.pkl"))
calorie_model = joblib.load(os.path.join(ML_DIR, "calorie_model.pkl"))
split_model = joblib.load(os.path.join(BASE_DIR, "ml", "split_model.pkl"))
days_model = joblib.load(os.path.join(BASE_DIR, "ml", "days_model.pkl"))

# ---------------- ROUTES ----------------

@app.route("/")
def home():
    return render_template("home.html", title="Home", page_class="home-bg")


@app.route("/workout")
def workout_page():
    return render_template("index.html", title="Workout Tracker", page_class="workout-bg")


@app.route("/history")
def history():
    return render_template("history.html", title="Workout History", page_class="history-bg")


@app.route("/bmi", methods=["GET"])
def bmi_page():
    return render_template("bmi.html", title="BMI Calculator", page_class="bmi-bg")


@app.route("/bmi/calculate", methods=["POST"])
def bmi_calculate():
    height_cm = float(request.form["height"])
    weight = float(request.form["weight"])

    height_m = height_cm / 100
    bmi = round(weight / (height_m ** 2), 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return jsonify({
        "bmi": bmi,
        "category": category
    })


# ✅ ML PREDICTION
@app.route("/ml-predict", methods=["POST"])
def ml_predict():
    height = float(request.form["height"])
    weight = float(request.form["weight"])
    bmi = float(request.form["bmi"])

    features = [[height, weight, bmi]]

    goal = goal_model.predict(features)[0]
    calories = int(calorie_model.predict(features)[0])
    split = split_model.predict(features)[0]
    days = int(days_model.predict(features)[0])
    return jsonify({
        "goal": goal,
        "calories": calories,
        "split": split,
        "days": days
    })



@app.route("/about")
def about():
    return render_template("about.html", title="About Me", page_class="about-bg")


if __name__ == "__main__":
    app.run()
