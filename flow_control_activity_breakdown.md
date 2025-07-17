# Vending Machine Program - Code Breakdown

# Set Up the Product Menu
    items = {
        "soda": 1.50,
        "chips": 2.00,
        "candy": 1.00,
        "nuts": 1.75,
        "water": 1.50,
## Creates a dictionary called items. Each key is a product name (string). Each value is the price of that product (float). 

# Prompt for Initial Funds     
    funds = float(input("How much money are you inserting into the machine? $"))

## Asks the user to input the amount of money they want to insert.
## input() gets the user’s answer as a string.
## float() converts the string to a number with decimals (like 2.00 or 5.50).
## The result is stored in the variable funds.   

# Display the Menu
    print("\nAvailable Items:")
    for item, price in items.items():
        print(f"- {item.title()}: ${price:.2f}")
    print(f"Current Balance: ${funds:.2f}")
## Loops through the items dictionary:For each item, prints the item name (with first letter capitalized) and its price (2 decimal places).
## Shows the current balance (money inserted by the user).

# Transaction Process
purchased_items = []  # Optional: To record each purchase
## Creates an empty list to keep track of items the user buys.


while funds > 0:
    choice = input("\nWhat would you like to buy? (type item name): ").lower().strip()
## Start a loop that continues as long as funds is greater than 0.
## Each time through the loop: Asks the user which item they want to buy and converts the answer to lowercase and removes extra spaces.


    if choice not in items:
        print("Sorry, that item isn't available. Please choose from the menu.")
        continue
## Checks if the user’s choice is in the menu (items dictionary).
## If not, prints an error and restarts the loop to ask again.


    price = items[choice]
    if funds >= price:
        funds -= price
        purchased_items.append(choice)  # Optional: Record purchase
        print(f"Dispensing {choice.title()}! Your new balance is: ${funds:.2f}")
## Gets the price of the chosen item.
## If the user has enough money (funds >= price):
## Deducts the item price from the balance.
## Adds the item to the purchase history (purchased_items).
## Prints confirmation and the updated balance. 

    else:
            print(f"Insufficient funds for {choice.title()}. You have ${funds:.2f}, but need ${price:.2f}.")
            more_money = input("Would you like to add more money? (yes/no): ").lower().strip()
            if more_money == "yes":
                extra = float(input("How much more would you like to add? $"))
                funds += extra
                print(f"New balance: ${funds:.2f}")
                continue
            else:
                print("Cancelling transaction.")
                break
## If the user doesn’t have enough money:
## Tells them how much they need and what they have.
## Asks if they want to add more money.
## If yes: asks how much, adds it to their funds, shows new balance, and restarts the loop.
## If no: prints a message and breaks out of the loop (ends transactions).                

 another = input("Would you like to buy another item? (yes/no): ").lower().strip()
    if another != "yes":
        break
## After a successful purchase, asks if the user wants to buy another item.
## If the answer is not "yes", the loop ends (no more transactions).

# Final Summary
print("\nThank you for using the vending machine!")
print(f"Your final balance is: ${funds:.2f}")

## Prints a thank-you message and the remaining balance (money left after shopping).

if purchased_items:
    print("You bought:")
    for item in purchased_items:
        print("-", item.title())
    total_spent = sum(items[item] for item in purchased_items)
    print(f"Total spent: ${total_spent:.2f}")
else:
    print("You didn't buy anything this time.")

## If the user bought any items:
## Prints "You bought:" and lists each purchased item.
## Calculates and prints the total money spent.
## If nothing was bought: Prints a message saying so.

print(f"Change returned: ${funds:.2f}")
print(" ")
print("Have a great day!")

## Prints the final change returned to the user (same as their balance).
## Prints a blank line for spacing.
## Prints "Have a great day!" to finish the program.