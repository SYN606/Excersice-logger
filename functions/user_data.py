from functions.save_data import save_data


# Simple color helper
def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"


def user_data():
    while True:
        name = input(color_text("Enter your Name: ",
                                "1;33")).strip()  # Bold Yellow
        meal = input(color_text("Enter your meal: ", "1;33")).strip()
        exercise = input(color_text("Enter your exercise for today: ",
                                    "1;33")).strip()

        print(
            color_text(
                f"\nYour details are:\nName: {name}\nMeal: {meal}\nExercise: {exercise}",
                "0;37"  # White
            ))

        try:
            response = int(
                input(color_text("Press 1 to confirm, 2 to edit: ", "1;33")))
        except ValueError:
            print(color_text("Invalid input. Please enter 1 or 2.",
                             "1;31"))  # Bold Red
            continue

        if response == 1:
            save_data(name, meal, exercise)
            break
        elif response == 2:
            print(color_text("\nEditing details...\n", "1;36"))  # Bold Cyan
        else:
            print(color_text("Invalid choice. Try again.", "1;31"))  # Bold Red
