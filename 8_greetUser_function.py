#!/usr/bin/env python3

def greetUser():
	myName = input("Enter username : ")

	if myName == "Alice":
		print("Hello Alice !! ")
	else:
		print("Hello " + myName)
		print("Welcome to Python programming !! ")
	storedPassword = "qwert"
	password = input("Enter your password : ")
	if password != storedPassword :
		print("Incorrect Password. Please try again.")
	else: 
		print("Welcome Alice!")
	return
greetUser()
