from functions.user_data import user_data
from functions.print_details import print_details
from functions.delete_user import delete_user


# Simple color helper
def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"


def main():
    print(color_text("Welcome to the Health Management System.\n",
                     "1;36"))  # Bold Cyan
    while True:
        try:
            choice = int(
                input(
                    color_text(
                        "1. Add your data\n2. View your data\n3. Delete user data\n4. Exit\nChoose: ",
                        "1;33")  # Bold Yellow
                ))
        except ValueError:
            print(color_text("Please enter a valid number.",
                             "1;31"))  # Bold Red
            continue
        except (KeyboardInterrupt, EOFError):
            print("\n" + color_text("Exiting the program. Goodbye!", "1;32"))
            break

        if choice == 1:
            user_data()
        elif choice == 2:
            print_details()
        elif choice == 3:
            delete_user()
        elif choice == 4:
            print(color_text("Exiting the program. Goodbye!",
                             "1;32"))  # Bold Green
            break
        else:
            print(color_text("Invalid choice.", "1;31"))  # Bold Red


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n" + color_text("Exiting the program. Goodbye!", "1;32"))
