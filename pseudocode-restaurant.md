# Pseudocode: Restaurant Ordering System

## 1. Start

## 1. Display Welcome Message
Display "Welcome to Python's Pancakes! We're happy to serve you."

## 1. Display Menu Items
Set menu = [
    ("Pancakes", 5.00)
    ("Omelette", 7.50)
    ("French Toast", 6.50)
    ("Coffee", 2.00)
    ("Orange Juice", 2.50)
    ("Bagel with cream cheese", 3.75)
    ("Steelcut Oats with berries", 4.25)
]

Display "Here is our menu:"
For each (item, price) in menu:
    Display item + "- $" + price

## 4. Initialize Empty Order / "Place Order" option
Set order = empty list

## 5. Ordering Loop
Repeat:
  ### a. Prompt Menu Selection
  Ask user: "Please type the name of the item you want to order:"
  Save input as selected_item

  ### b. Validate Selection
  If selected_item is not in menu:
      Display "Sorry, we don't have that item. Please choose from the menu."
      Go back to Prompt Menu Selection

  ### c. Prompt Quantity
  Ask user: "How many [selected_item] would you like?"
  Save input as quantity

  ### d. Add to Order
  Add (selected_item, quantity) to order list

  ### e. Continue Ordering?
  Ask user: "Would you like to order another item? (yes/no)"
  If answer is "yes", repeat loop
  If answer is "no", exit loop