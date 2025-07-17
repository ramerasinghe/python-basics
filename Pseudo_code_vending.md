Pseudocode for Vending Machine Program

1. Set up the product menu:
Create a dictionary of items and prices

1. Prompt for initial funds
Prompt user: "How much money are you inserting into the machine?"

Save user input as starting balance

1. Display the menu:
Show each item with its price

Show current balance

1. Begin transaction process:
WHILE user has funds > 0
a. Prompt user: "What would you like to buy?"

b. IF item not in menu:
- Tell user it's unavailable
- Continue to next loop iteration

c. IF user has enough funds for item:
- Subtract price from balance
- Add item to purchased list
- Tell user it's dispensed and show new balance

d. ELSE (not enough funds):
- Tell user not enough funds, show required amount
- Ask if they want to add more money
i. IF yes:
- Prompt for amount, add to balance, continue
ii. IF no:
- Cancel transaction, break loop

e. Ask user if they want to buy another item
- IF "yes", continue
- ELSE, break loop

1. Show summary:
Thank the user

Show final balance

IF any items bought, show each, and total spent

ELSE, say "You didn't buy anything this time"

Show "change returned" and a goodbye message