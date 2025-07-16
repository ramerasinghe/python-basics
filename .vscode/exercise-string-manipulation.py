# Split a string into individual values

to_be_changed = "John Glenn|Neil Armstrong|Sally Ride|Douglas Wheelock|Mae Jemison"
changed_values = to_be_changed.split("|")
print(changed_values)

# Split lyrics by line using split()

lyrics = """
Katie Casey was baseball mad,
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "No,
I'll tell you what you can do:"
"""
lyrics_split = lyrics.split("\n")
print(lyrics_split)

# How long is the long village name string?

lyrics = """
Katie Casey was baseball mad,
Had the fever and had it bad.
Just to root for the home town crew,
Ev'ry sou
Katie blew.
On a Saturday her young beau
Called to see if she'd like to go
To see a show, but Miss Kate said "No,
I'll tell you what you can do:"
"""
changed_values = lyrics.splitlines()
print(changed_values)

long_village_name = "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
string_length = len(long_village_name)
print(string_length)

# Get all folders in a path without additional spaces

my_path = ' /c/Users/instructor/Downloads/Submit Relating the Nonrelational Assessment Download May 10, 2021 917 AM '
my_folders = my_path.strip().split("/")
print(my_folders)

# Change the third name in the list to "Wolfgang Mozart"

composers="Beethoven,Ludwig von;Liszt,Franz;Mozart,Wolfgang;Copland,Aaron"
composers = composers.replace('Mozart,Wolfgang', 'Wolfgang Mozart')
print(composers)

# Separate the composers
composers_split = composers.split(";")
print(composers_split)

# Get the third composer
third_composer = composers_split[2]
print(third_composer)

# Find the comma in the name
comma_position = third_composer.find(",")
print(comma_position)

# Join the names to get the 3rd composer's name in "first last" format
first_name = "Wolfgang"
last_name = "Mozart"
full_name = first_name + " " + last_name
third_composer_name = print(f"{first_name} {last_name}")
print(full_name)

# Print the composer's name
print(third_composer_name)

# Clean padded strings

left_padded = 'Operators are standing by'
right_padded = 'Call now '
cleaned = right_padded.rstrip() + '!' + left_padded
print(cleaned)

# Print student info using old-style formatting

student_name = "Owen"
grade = 94.75
assignment_number = 12
print('Student name: %s, Assignment ID: %04d, Grade: %.2f%%' % (student_name, assignment_number, grade))

# Pad employee ID with zeroes to 6 digits

employee_id = "30"
employee_id_padded = employee_id.zfill(6)
print(employee_id_padded) 
