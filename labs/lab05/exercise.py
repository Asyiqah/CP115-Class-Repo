# Lab 05 - practice file
#
# Use this file to try out the examples as you work through the lab.
# Type them in, run the file, then clear it out and use it again for the next one.
#
# Run it from the terminal with:   python exercise.py
# On Windows you may need:         py exercise.py
#
# Nothing in this file is marked, so experiment as much as you like.

# Examples of valid identifiers and variables
student_name = "Alice"
age = 20
total_score = 95.5
is_enrolled = True
course_code = "CP115"

# Examples of identifier naming conventions
firstName = "John"        # camelCase (less common in Python)
first_name = "Jane"       # snake_case (Python convention)
MAXIMUM_ATTEMPTS = 3      # UPPER_CASE for constants

# Let's see Python keywords
import keyword
print(keyword.kwlist)

# Numeric data types
age = 21                    # int (integer)
height = 5.9               # float (floating-point number)
temperature = -15.5        # float (can be negative)

# String data type
student_name = "Muhammad Ali"    # str (string)
course_title = 'Python Programming'  # str (single or double quotes)
description = """This is a multi-line
string that spans several lines."""   # str (triple quotes)

# Boolean data type
is_active = True           # bool (boolean)
has_submitted = False      # bool (boolean).

# Special data type
nothing = None             # NoneType (represents absence of value)

print(type(age))             #int
print(type(temperature))     #float
print(type(student_name))    #string
print(type(is_active))       #boolean
print(type(nothing))         #nonetype

print(type(25))
print(type("25"))

number_text = "25"
print(type(number_text))

real_number = int(number_text)
print(type(real_number))

text = "Hello World"

# len() is a function, so the value goes inside the brackets
print(len(text))          # 11

# upper() and lower() are methods, so the value comes before the dot
print(text.upper())       # HELLO WORLD
print(text.lower())       # hello world

len( text )
text . upper()

text = "Hello World"

print(text.upper())
print(text.upper)

text = "hello"
text.upper()
print(text)               # hello

text = "hello"
shouted = text.upper()

print(text)               # hello
print(shouted)            # HELLO

text = "hello"
text = text.upper()
print(text)               # HELLO

# Import entire modules
import math
import random
import datetime

# Using imported modules
circle_area = math.pi * (5 ** 2)
random_number = random.randint(1, 100)
current_date = datetime.date.today()

# Import specific functions from modules
from math import sqrt, pow, sin, cos
from random import choice, shuffle
from datetime import datetime, timedelta

# Using imported functions directly (no module prefix needed)
square_root = sqrt(25)
power_result = pow(2, 8)
random_choice = choice(['apple', 'banana', 'cherry'])

age = input("Enter your age: ")
print(age)
print(type(age))

first = input("First number: ")
second = input("Second number: ")
print(first + second)

first = int(input("First number: "))
second = int(input("Second number: "))
print(first + second)

print("Hello", "Python", "World")
print("Hello", "Python", "World", sep="-")

print("Hello", end=" ")
print("World")

name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")