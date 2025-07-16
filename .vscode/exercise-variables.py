# 1: Create a variable named "onomatopoeia" and set its value to 'pop'. Print the type of onomatopoeia.

onomatopoeia = 'pop'
print(type(onomatopoeia)) 

# 2: Create a variable named "lyrics" and assign it the following multiline string:

lyrics = """Katie Casey was baseball mad, 
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "No,
I'll tell you what you can do:"""
print(lyrics)

# 3: Create a variable named "gpa" and set it to "3.75". Print the variable and its type.

gpa = 3.75
print(gpa)
print(type(gpa))

# 4: Create a variable named "empty_var" and assign it the Python equivalent of null. Print the variable and its type.

empty_var = None
print(empty_var)
print(type(empty_var))

# 5: Create a variable that stores the value of 828^282. Print the variable.

Large_integer = 282 ** 282
print(Large_integer)

# 6: Store the result of the Math Expression

result = (52 - 52) + (64 / 8) + (42 % 8)
print(result) 

# 7: Boolean Variables

my_boolean = True
my_is_true = (my_boolean is not False)
print(my_is_true)
print(type(my_is_true))

# 8: String Comparison 

weird_word = "Weird"
is_match = (weird_word == "weird")
print(is_match)

# 9: Create a variable named false. 

false = False
print(False)

# shows: NameError: name 'false' is not defined. Did you mean: 'False'?
# shows: SyntaxError: cannot assign to False
# False cannot be used as a variable because it is a reserved word in Python.

# 10: Complete math equations

num1 = 35 / 7
num2 = 15 ** 3
num3 = num2 % num1
num4 = num2 / num1
print(num1)
print(num2)
print(num3)
print(num4)
