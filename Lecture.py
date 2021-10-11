# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# concatonate 
print("Cat")
print("Cat" + " videos")

print("Cat" * 3)
print("Cat" + str(3))

print("Cat".upper())
print("Cat".lower())

print("the lord of the rings".title())

# String formatting

oranges = 12
cost_per_orange = 0.5
total_cost = oranges * cost_per_orange
output = "{} oranges costs £{}".format(oranges, total_cost)
print(output)

print(f"{oranges} oranges cost £{total_cost}")

# Exercise

# create a program that calculates how many cans of food you need to feed 10 cats

cats = 10
# cans is a variable which refers to the number of cans eaten by 1 cat per day
cans = 3
total_cans = cats * cans
total_cans_week = total_cans * 7

# 1 way to print
print(f"{cats} cats need {total_cans} cans per day")

# using format method to print
print("{} cats need {} cans per day".format(cats, total_cans))

# extension
print(f"{cats} need {total_cans_week} cans to survive for 7 days")

# exercise

guests = ["Mary", "Pete", "Eoin"]
separator = ', '
print("We are going to cinema with my classmates:", separator.join(guests), "and me.")

# Andree's way of doing it

print("We are going to cinema with my classmates: {names} and me.".format(names=', '.join(guests)))

# slicing
S = 'ABCDEFGHI'
print(S[0:3])
print(S[-3:])

# Reverse a string
S = 'ABCDEFGHI'
print(S[::-1])

# EXERCISE
S = 'ABCDEFGHI'

# Slice last three characters from the string
print(S[0:6])
print(S[-9:-3])
# not sure if i understood the assignment
print(S[6:9])
print(S[-3:])
# Slice from beginning to end with step 2:
print(S[0:9:2])
print(S[-9::2])
#Get CD using 4 different slicing ways:
print(S[2:4])
print(S[-7:-5])
# the following two are a combination of positive and negative indexing
print(S[2:-5])
print(S[-7:4])

# SOLUTIONS FROM SLACK

### DEMO 1 ###
​
"""
print('Hello, World!')
print('I hope it is sunny this weekend')
"""
# ​
### EXERCISE 1 ###
# ​
# """
# Exercise 1.1: Now that you've run your first program, try the following:
# ​
# - Change the message to anything you want
# - Repeat the code on multiple lines to output several messages
# - Find out what happens when you remove different parts of the code (e.g. brackets)
# - Don't worry if something unexpected happens. Think about what you changed and why it might have caused it to happen.
# """
# ​
### DEMO & EXERCISE 2 ###
# ​
# """
# Practice the following operations in the console:
# ​
5 - 6
8 * 9
6 / 2
5 / 0	# zero division error
5.0 / 2
5 % 2
2 * (10 + 3)
2 ** 4
# ​
# What does each one do and what is its output?
# Are there any outputs you didn't expect?
# """
# ​
### DEMO & EXERCISE 3 ###
# ​
# """
# In your Python console type each of these
# ​
print("Cat")
"Cat" + " videos"
# ​
"Cat" * 3
"Cat" + 3
# ​
"Cat".upper()
"Cat".lower()
# ​
"the lord of the rings".title()
# ​
# What is the output for each one and why?
# One of them causes an exception. Read the exception message. What do you think it means?
# """
# ​
### DEMO & EXERCISE 4 ###
# ​
# """
# EXAMPLES OF STRINGS METHODS
# ​
# 'Our example string object'.upper()
# 'Our example string object'.lower()
# 'Our example string object'.title()
# 'Our example string object'.count('o')
# 'our example string object'.capitalize()
# 'Our example string object'.endswith('ject')
# 'Our example string object'.endswith('mock')
# 'To make a nice cuppa you need: tea, milk, sugar and a cookie '.split(',')
# 'Our example string object'.replace('p', '#')
# ​
# Check built in methods available to use for strings
# ​
'string object' + . + click TAB
use help() function
# """
# ​
# ### EXERCISE 5 ###
# ​
# """
# Errors and casting objects into different types
# ​
# Run this:
# ​
print("Cat" + 3)
# ​
# it would result in Error!
# Putting a number in str() converts it to a string
# ​
print("Cat" + str(3))
# """
# ​
# ### DEMO 6 ###
# ​
# """
oranges = 12
cost_per_orange = 0.5

total_cost = oranges * cost_per_orange

print(str(oranges) + " oranges")
print("costs " + str(total_cost))
# ​
# The oranges variable is reused twice in the program
# """
# ​
# ### EXERCISE 7 ###
# ​
# """
# In a new Python file called cat_food.py, create a program that calculates how many cans of cat food you need to feed 10 cats
# ​
# Your will need:
# ​
# A variable for the number of cats
# A variable for the number of cans each cat eats in a day
# A print() function to output the result
# Extension: change the calculation to work out the amount needed for 7 days
# ​
# --------------------
# Example solution below
# ​
cats = 10
cans = 2

total_cans = cats * cans

output = str(cats) + " cats eat " + str(total_cans) + " cans"
print(output)
# ​
# """
# ​
# ### EXERCISE 7 ###
# ​
# """
# Rewrite cat_food.py to use string formatting instead of joining strings with +.
# ​
# An example of string formatting:
# --------------------------------
# ​
user_name = 'Jenny_1995'
age = 23
# ​
output = '{} is {} years old'.format(user_name, age)
print(output)
# ​
#-----------------
# Example solution
​
cats = 10
cans = 2

total_cans = cats * cans

output = "{} cats eat {} cans".format(cats, total_cans)
print(output)
# """
# ​
# ### DEMO 8 ###
# ​
# """
# Show few examples on how to join strings together:
# ​
'-'.join(my_words)
' '.join(my_words)
''.join(my_words)
# """
# ​
# ### EXERCISE 8 ###
# ​
# """
# Perform string formatting, so that your final sentence looks like this:
guests = ["Mary", "Pete", "Eoin"]
# ​
# Result:
"We are going to cinema with my classmates: Mary, Pete, Eoin and me"
# ​
# Example solution below:
# (We can use string interpolation and join() function to build this sentence)
# ​
guests = ["Mary", "Pete", "Eoin"]
# ​
print("We are going to cinema with my classmates: {names} and me.".format(names=', '.join(guests)))
# """
# ​
### DEMO & EXERCISE 9 ###
# ​
# """
# ​
S = 'ABCDEFGHI'
print(S[2:7])
# ​
S = 'Hippopotamus'
print(S[-7:-2])
# ​
S = 'ABCDEFGHI'
print(S[2:-5])
print(S[2:4])
print(S[-7:-5])
# ​
S = 'ABCDEFGHI'
print(S[::2])
# ​
# ​
# Slice at Beginning & End
# ​
# Omitting the start index starts the slice from the index. Meaning, S[:stop] is equivalent to S[0:stop]
# Omitting the stop index extends the slice to the end of the string. Meaning, S[start:] is equivalent to S[start:len(S)]
# ​
# Slice first three characters from the string
S = 'ABCDEFGHI'
print(S[:3])
# ​
# ​
# Slice last three characters from the string
S = 'ABCDEFGHI'
print(S[6:])
# ​
# ​
# Reverse a String
# You can reverse a string by omitting both start and stop indices and specifying a step as -1.
# ​
S = 'ABCDEFGHI'
print(S[::-1])
# ​
S = 'Code First Girls'
print(S[::-1])
# """
# ​
# ## DEMO 10 ###
# ​
# """
# In built functions examples
# Comment / uncomment each line in turn to see what each in-built function does
# ​
print('Code')
type('Code')
len('Code')
ord('C')
chr(ord('C'))
help('Code')
help(type('Code'))
"""