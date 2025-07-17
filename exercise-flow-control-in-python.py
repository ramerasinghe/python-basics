# Set Up the Product Menu
items = {
    "soda": 1.50,
    "chips": 2.00,
    "candy": 1.00,
    "nuts": 1.75,
    "water": 1.50,
}

# Prompt for Initial Funds
funds = float(input("How much money are you inserting into the machine? $"))

# Display the Menu
print("\nAvailable Items:")
for item, price in items.items():
    print(f"- {item.title()}: ${price:.2f}")
print(f"Current Balance: ${funds:.2f}")

# Transaction Process
purchased_items = [] 

while funds > 0:
    choice = input("\nWhat would you like to buy? (type item name): ").lower().strip()

    if choice not in items:
        print("Sorry, that item isn't available. Please choose from the menu.")
        continue

    price = items[choice]
    if funds >= price:
        funds -= price
        purchased_items.append(choice)  
        print(f"Dispensing {choice.title()}! Your new balance is: ${funds:.2f}")
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

    another = input("Would you like to buy another item? (yes/no): ").lower().strip()
    if another != "yes":
        break

# Final Summary
print("\nThank you for using the vending machine!")
print(f"Your final balance is: ${funds:.2f}")

if purchased_items:
    print("You bought:")
    for item in purchased_items:
        print("-", item.title())
    total_spent = sum(items[item] for item in purchased_items)
    print(f"Total spent: ${total_spent:.2f}")
else:
    print("You didn't buy anything this time.")

print(f"Change returned: ${funds:.2f}")
print(" ")
print("Have a great day!")

