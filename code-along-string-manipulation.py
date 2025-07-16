string1 = 'This is a valid string'
string2 = "This is also a valid string"
# string3 = 'This is NOT a value string - see why?"

palindrome = "Go hang a salami, I'm, a lasagna hog"

# Using a quote inside string

string3 = "'Always look on the bright side of life' - Monty Python"

# Use escape characters to include quotes in strings

string4 = "\"Always look on the bright side of life\" - Monty Python"
print(string4)

# len() function
# strip() function

len(string4)
print(len(string4))

name = "    Michael   "
print(len(name))
print("Hello" + name)

name_no_spaces = name.strip()
print(len(name_no_spaces))
print("Hello " + name_no_spaces)

# split()

filepath = "/var/michael/here"
folders = filepath.split("/")
print(folders)
print(type(folders))

fullname = "Michael,Vanderpool"
names = fullname.split(",")
row = "Michael Vanderpool, 49, 6'4\""

# print(name): ['Michael', 'Vanderpool']
firstname = names[0]
lastname = names[1]

print("First name: " + firstname)
print("Last name: " + lastname)

#join

windowsPath = "||".join(folders)
print(windowsPath) 

# find()

reservation_name = "Froman, Abe"
char_to_find = ","
# Where is the comma?

char_location = reservation_name.find(char_to_find)
print(char_location)

# index()
char_location = reservation_name.find(char_to_find)
print(char_location)

# transformations

print(reservation_name.upper())
print(reservation_name.lower())
print(reservation_name.title())
print(reservation_name.swapcase())
print(reservation_name.capitalize())

# f-strings

name = "Michael"
age = 49

print(f"My name is {name} and I am {age} years old.")
print("My name is " + name + " and I am " + str(age) + " years old.")

a = 3
b = 9
print(f'We can countr to {b} by {a}: {a} {a*2} {a*3}')

# replacing

name = "Micael Vanderpoole"
name = name.replace("Micael", "Michael")
name = name.replace("Vanderpoole", "Vanderpool")
print(name)

