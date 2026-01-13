import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
import joblib
import os

# Base directory
BASE_DIR = os.path.dirname(__file__)
csv_path = os.path.join(BASE_DIR, "fitness_data.csv")

# Load dataset
data = pd.read_csv(csv_path)

# ✅ FINAL FEATURES (3 ONLY)


# Features
X = data[["height", "weight", "bmi"]]

# Targets
y_goal = data["goal"]
y_cal = data["calories"]
y_split = data["split"]
y_days = data["days"]

goal_model = DecisionTreeClassifier(max_depth=5)
goal_model.fit(X, y_goal)

split_model = DecisionTreeClassifier(max_depth=4)
split_model.fit(X, y_split)

days_model = DecisionTreeClassifier(max_depth=3)
days_model.fit(X, y_days)

cal_model = LinearRegression()
cal_model.fit(X, y_cal)

# Save models INSIDE ml folder
joblib.dump(goal_model, os.path.join(BASE_DIR, "goal_model.pkl"))
joblib.dump(cal_model, os.path.join(BASE_DIR, "calorie_model.pkl"))
joblib.dump(split_model, os.path.join(BASE_DIR, "split_model.pkl"))
joblib.dump(days_model, os.path.join(BASE_DIR, "days_model.pkl"))



print("✅ Models trained and saved successfully")
