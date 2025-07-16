# play with for loops

# create a list

# use a for loop to iterate through the list



# create an empty meal prep list

meal_prep_list = []
print("Your meal prep list:", meal_prep_list)

# append meals to the list

meal_prep_list.append("Grilled chicken with rice and broccoli")
meal_prep_list.append("Salmon with sweet potatoes and asparagus")

print("Updated meal prep list:", meal_prep_list)

# insert a meal at the beginning

meal_prep_list.insert(0, "Egg muffins with spinach and feta")
print("After inserting a breakfast meal:", meal_prep_list)

# update an existing list

print(meal_prep_list[0])
meal_prep_list[0] = "Breakfast - Egg muffins with spinach and feta"
meal_prep_list[1] = "Lunch - Grilled chicken with rice and broccoli"
meal_prep_list[2] = "Dinner - Salmon with sweet potatoes and asparagus"
print("Updated meal_prep_list:", meal_prep_list)


# Print current meal prep list

print("Current meal_prep_list:", meal_prep_list)

# Pop (remove) the lunch meal (index 1)

eaten_meal = meal_prep_list.pop(1)
print("You ate:", eaten_meal)
print("Meal prep list after removal:", meal_prep_list)


# Add a snack to the end of the list

meal_prep_list.append("Snack - Greek yogurt with berries")
print("After adding a snack:", meal_prep_list)

# for loop to print each meal

for meal in meal_prep_list:
    print("Meal prep option:", meal)

print("This week's meals:")
for meal in meal_prep_list:
    print("-", meal)