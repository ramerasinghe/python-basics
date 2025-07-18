# functions — anything with () — are resuable pieces of code!

def greet(name):
    name = name.lower()
    name = name.capitalize()
    print(f"Hello, {name}! Welcome to the party!")

def user_input():
    input_value = input(prompt)

def main_menu():
    print("Welcome to the main menu")
    print("1. Start")
    print("2. Exit")

    choice = input("Please choose an option: ")
    print(f'You chose option {choice}')
    return choice

print("Hello!")
print("My name is Python.")
greet("Mike")


main_menu_choice = main_menu()

if main_menu_choice == 1:
    print("Starting the program...")

