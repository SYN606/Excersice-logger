import json
import os

DATA_DIR = "data"


# Simple color helper
def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"


def print_details():
    name = input(color_text("Enter your name: ",
                            "1;33")).strip()  # Bold Yellow
    file_path = os.path.join(DATA_DIR, f"{name}.json")

    if not os.path.exists(file_path):
        print(color_text("User not found.", "1;31"))  # Bold Red
        return

    try:
        with open(file_path, "r") as f:
            records = json.load(f)
    except json.JSONDecodeError:
        print(color_text("Corrupted data file.", "1;31"))  # Bold Red
        return

    print(color_text("\nYour Records:", "1;36"))  # Bold Cyan
    for entry in records:
        print(
            color_text(
                f"- {entry['date']} | Meal: {entry['meal']} | Exercise: {entry['exercise']}",
                "0;37"  # White
            ))
