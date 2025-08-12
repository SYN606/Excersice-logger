import json
import os
from functions.get_date import get_date

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)


def save_data(name, meal, exercise):
    file_path = os.path.join(DATA_DIR, f"{name}.json")

    # Load existing data if file exists
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                records = json.load(f)
            except json.JSONDecodeError:
                records = []
    else:
        records = []

    # Append new entry
    records.append({"date": get_date(), "meal": meal, "exercise": exercise})

    # Save back to file
    with open(file_path, "w") as f:
        json.dump(records, f, indent=4)

    print("\n Data successfully saved!")
