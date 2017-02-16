import json

#### PART I: ####
f = open("person.json", "r")
person = json.load(f)
f.close()

# Task 1:
# person is a variable that loads a json object from a text file using json module
# Please identify the data type of person by using print method
print("\n----Task 1----")
# TODO:: Your code starts here:

# Task 2:
# Iterate through the variable "person", and print out the keys
# Example Output:
# name
# age
# ...
print("\n----Task 2----")
# TODO:: Your code starts here:

# Task 3:
# By modifying the code you have from task 3, print out the data type of the
# value that associate with each key
# Example Output:
# name: type(<class 'str'>)
# age: type(<class 'int'>)
# ...
print("\n----Task 3----")
# TODO:: Your code starts here:

# Task 4:
# Print the person's name
print("\n----Task 4----")
# TODO:: Your code starts here:

# Task 5:
# Print all of the item under 'numbers'. One items per line
#
# The output should be:
# 1
# 3
# 5
# 3
# 9

print("\n----Task 5----")
# TODO:: Your code starts here:

# Task 6:
# List all of the class name under course_taken
#
# hint: course_taken returns a dictionary, how can you iterate through it?
#
# The output should be:
# Example Course
# Test Course 2
print("\n----Task 6----")
# TODO:: Your code starts here:

#### PART II: ####
f = open("studygroup.json", "r")
studygroup = json.load(f)
f.close()

# Task 7:
# studygroup is a variable that loads a json object from a text file using json module
# Print out the data type of the value that associate with each key
# Example Output:
# name: type(<class 'str'>)
# meeting_time: type(<class 'str'>)
# ...
print("\n----Task 7----")
# TODO:: Your code starts here:

# Task 8:
# Iterate through members, list all the member's name
# hint: is studygroup["members"] returns a list or dict? How can you iterate
# through it?
print("\n----Task 8----")
# TODO:: Your code starts here:

# Task 9:
# Create a new dictionary called member_data, which use each member's name as key
# and the value should be a list contains books that person has read
# Example for a single entry
# "nameA" : ["Book A", "Book B"]
# Hint: You can print member_data by using
#       print(json.dumps(member_data, indent=2))
print("\n----Task 9----")
# TODO:: Your code starts here:

# Task 10:
# Write member_data to a text file called member_data.json
# hint: you can use json.dumps(data) to get a string. data is a dictionary
print("\n----Task 10----")
# TODO:: Your code starts here:

print("\n----End----")
