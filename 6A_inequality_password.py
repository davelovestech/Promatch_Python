#!/usr/bin/env python3

correct_password = "password"

entered_password = input("What is the password? ")

if correct_password != entered_password:
	print("incorrect password")
if correct_password == entered_password:
	print("correct password")
