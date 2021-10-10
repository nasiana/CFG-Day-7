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