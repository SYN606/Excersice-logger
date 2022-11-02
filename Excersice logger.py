# creating a health management system and saving it in a {.txt} file
# --> what they eat 
# --> what excercise they do 



import datetime


def getdate():
    return datetime.date.today()

today = getdate()

print(today)

#  getting user data and writing it into a .txt file.

def user_data():
    name = input("Enter your Name : ")
    meal = input("Enter you meal : ")
    excersice = input("Enter your excersice that you done today : ")

    print(f"\nYour details are : \n{name}, your meal is {meal} and you done {excersice}.\nconfirm your details by pressing 1 or edit your details by pressing 2.")

    response = int(input())
    while True:
        if response == 1: # --> saving data into .txt file.
            with open(name + ".txt", "a") as f:
                f.write(f"{name}, your meal is {meal} and you done {excersice} excersice {today}.")
                f.write("\n")
            print("\nSuccesfully saved.")
            break

        elif response == 2: # --> editing and then saving data into python file.
            name = input("Edit your Name : ")
            meal = input("Edit you meal : ")
            excersice = input("Edit your excersice that you done today : ")
            print(f"\nNow your name is {name}, your meal is {meal}, and you done excersice {today} is {excersice}")

            with open(name + ".txt", "a") as f:
                f.write(f"{name}, your meal is {meal} and you done {excersice} excersice {today}.")
                f.write("\n")
            print("\nSuccessfully edited and saved.")
            break
        
        else:
            print("Something went wrong, Plese choose the correct option.")



# printing user data

def print_details():
    name = input("Enter your name : ")

    try:
        with open(name + ".txt", "r") as f:
            log = f.readlines()
            log = ''.join(log) # --> converting list into string
            print(log)
    except:
        print("User not found.")



print("Welcome to the health management system.\n")

while True:
    print("Please choose an option correctly.\n")
    opt_1 = int(input("Enter 1 for add your data, enter 2 for see your data : "))

    if opt_1 == 1:
        user_data()
        break

    elif opt_1 == 2:
        print_details()
        break
    else:
        print("Something went wrong please choose an option correctly.")