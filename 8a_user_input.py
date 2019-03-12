#!/usr/bin/env python3

# you can request user input with the input argument
name = input("What is your name? ")

print("Hello " + name + "! Welcome to Python!")

# here's a preview of equality comparisons
# they will be in the next section
if name == "David Halvorsen":
	print("you wrote this code!")

age = int(input("How old are you? "))
if age >= 18:
	print("You can vote! ")
