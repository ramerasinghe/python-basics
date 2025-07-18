# VARIABLES & IF STATEMENTS
favorite_color = "yellow"       # String variable
favorite_number = 2             # Integer variable
temperature = 98.2              # Float variable
tomorrow_is_Saturday = True     # Boolean variable     

print(favorite_color)
print(favorite_number)
print(temperature)
print(tomorrow_is_Saturday)


## String example
if favorite_color == "pink":            # 'if' checks if color = what variable is set to
    print("Yellow is a cool color!")    # what prints if color matches what variable is set to
else:                                   
    print("That's a nice color too!")   # what prints if color does NOT match what variable is set to


## Integer example 
if favorite_number == 2:                        # 'if' checks if number = what variable is set to
    print("That's my favorite number too!")     # what prints if number matches what variable is set to
else:
    print("That's a nice number!")              # what prints if number does NOT matche what variable is set to


## Float example
if temperature > 80.0:
    print("It's a hot day!")            # what prints if variable set is greater than the number provided
else:
    print("The weather is pleasant.")   # what prints if variable set is less than the number provided


## Boolean example
if tomorrow_is_Saturday:
    print("Yay! No school tomorrow!")       # what prints when boolean variable is set as 'true'
else:
    print("Better get ready for school.")   # what prints when boolean variable is set as 'false'


# INPUT & OUTPUT
tv_show = input("Enter your favorite tv show: ")      # Gets user input as a string
print("Wow! I like " + tv_show + " too!")           # Prints a message including their input


# TYPE CONVERSION
year = 2025 # sets the variable
year = int(input("What year are we in?: "))      # Converts input to an integer
print("Correct! Next year, it will be", year + 1)  # Prints the year plus one


#LISTS
vegetables = ["lettuce", "carrots", "broccoli"]     # Creates a list with three items — [] are used to create lists
vegetables.append("cauliflower")               # Adds "cauliflower" to the end
vegetables.remove("lettuce")                 # Removes "lettuce" from the list
print(len(vegetables))                    # 'Len" prints the number of items in the list / lists length


# LOOPS
number = 1                  # While loops starting point
while number <= 5:          # Repeats the loop as long as number is 5 or less
    print(number)
    number += 1             # Increase by 1 each loop


# FUNCTIONS
def greet(name):                    # defines a function named greet that takes one argument, name
    print("Hello," + name + "!")    # prints a greeting using that name

greet("Taylor")                     # calls the function with "Taylor"


## Function with Return Value
def multiply(x, y):                 # defines a function with two arguments
    return x * y                    # gives back the product of the two arguments

result = multiply(4, 5)
print(result)


