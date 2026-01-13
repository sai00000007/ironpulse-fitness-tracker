import random
import pandas as pd

rows = []

goals = ["Weight Loss", "Muscle Gain", "Maintenance"]
splits = {
    "Weight Loss": ["Full Body", "Upper Lower"],
    "Muscle Gain": ["Push Pull Legs", "Bro Split", "Upper Lower"],
    "Maintenance": ["Full Body", "Upper Lower"]
}

for _ in range(400):  # 🔥 change to 300/500 anytime
    height = random.randint(150, 190)
    weight = random.randint(45, 110)

    bmi = round(weight / ((height / 100) ** 2), 2)

    # Goal logic
    if bmi < 18.5:
        goal = "Muscle Gain"
    elif bmi < 25:
        goal = random.choice(["Maintenance", "Muscle Gain"])
    elif bmi < 30:
        goal = random.choice(["Weight Loss", "Maintenance"])
    else:
        goal = "Weight Loss"

    split = random.choice(splits[goal])

    # Training days logic
    if split == "Push Pull Legs":
        days = random.choice([5, 6])
    elif split == "Bro Split":
        days = 5
    elif split == "Upper Lower":
        days = random.choice([4, 5])
    else:
        days = random.choice([3, 4])

    # Calories logic (rough TDEE style)
    calories = int(
        (10 * weight) + (6.25 * height) - 5 * 25 + 5
    )

    if goal == "Weight Loss":
        calories -= random.randint(300, 500)
    elif goal == "Muscle Gain":
        calories += random.randint(300, 500)

    rows.append([
        height,
        weight,
        bmi,
        goal,
        calories,
        split,
        days
    ])

df = pd.DataFrame(rows, columns=[
    "height", "weight", "bmi", "goal", "calories", "split", "days"
])

df.to_csv("fitness_data.csv", index=False)

print("✅ fitness_data.csv generated with", len(df), "rows")
