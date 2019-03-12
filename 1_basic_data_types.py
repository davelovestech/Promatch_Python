#!/usr/bin/env python3

# a string is text enclosed in quotes
this_is_a_string = "this is a string"
# an integer is a number without decimal points
this_is_an_integer = 8
# a float has decimal points
this_is_a_float = 3.14159
# a boolean is a True or False value
this_is_a_boolean = True

# you can use the python type argument to
# get the type of a variable. Here I am printing
# each type
string_type = type(this_is_a_string)
print(string_type)

integer_type = type(this_is_an_integer)
print(integer_type)

float_type = type(this_is_a_float)
print(float_type)

boolean_type = type(this_is_a_boolean)
print(boolean_type)

# you can convert types into different types
# this is converted a string "8" to an int 8
looks_like_a_number = "8"
print(looks_like_a_number)
print(type(looks_like_a_number))
looks_like_a_number = int(looks_like_a_number)
print(looks_like_a_number)
print(type(looks_like_a_number))

# this is converting a number 8 to a string "8"
print(looks_like_a_number)
print(type(looks_like_a_number))
looks_like_a_number = str(looks_like_a_number)
print(looks_like_a_number)
print(type(looks_like_a_number))

# WE SHOULD ADD CONVERTING BETWEEN BOOLEAN/STRING
# AND FLOAT/INTEGER

