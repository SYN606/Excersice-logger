import os

DATA_DIR = "data"


# Simple color helper
def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"


def delete_user():
    name = input(color_text("Enter the name of the user to delete: ",
                            "1;33")).strip()
    file_path = os.path.join(DATA_DIR, f"{name}.json")

    if not os.path.exists(file_path):
        print(color_text("User not found.", "1;31"))  # Bold Red
        return

    confirm = input(
        color_text(
            f"Are you sure you want to delete all data for '{name}'? (y/n): ",
            "1;33")).strip().lower()
    if confirm == "y":
        try:
            os.remove(file_path)
            print(
                color_text(f"All data for '{name}' has been deleted.",
                           "1;32"))  # Bold Green
        except OSError as e:
            print(color_text(f"Error deleting file: {e}", "1;31"))
    else:
        print(color_text("Deletion cancelled.", "1;36"))  # Bold Cyan
