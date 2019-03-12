#!/usr/bin/env python3

a_string = 'this is a string'
print(a_string)
an_integer = 8
print(an_integer)
a_float = 3.14158
print(a_float)
a_boolean = True  # False
print(a_boolean)

print(type(a_string))
print(type(an_integer))
print(type(a_float))
print(type(a_boolean))

#Converting between types
new_float = float(an_integer)
print(new_float, type(new_float))

new_integer = int(a_float)
print(new_integer, type(new_integer))

new_string = str(a_float)
print(new_string, type(new_string))
