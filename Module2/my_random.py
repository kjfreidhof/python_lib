# Author: Kyle Freidhof
# Created: May, 25 2024
# LICENSE: MIT
# Credits: https://www.programiz.com/python-programming/examples/random-number
# About: A simple program to choose a random number between 0 and 1000

# Importing the random module
import random

# Defining the function as number
def number():
    # Storing 0 in x and then 1000 in y 
    x = 0
    y = 1000

    # Then print a random number between the to. 
    print(random.randint(x, y))

# Then execute the number function
number()
