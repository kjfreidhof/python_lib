# Author: Kyle Freidhof
# Created: May, 25 2024
# LICENSE: MIT
# Credits: https://www.programiz.com/python-programming/examples/square-root
# About: A simple program to solve the square root

# importing a python module cmath
import cmath 

# Defining the function main 
def main():
    # Asking for user input and then storing it in varriable n
    n = eval(input("Enter numbers: "))
    # Then in the varriable sqrt having cmath solve the square root 
    sqrt = cmath.sqrt(n)
    # Then print out the results
    print("The square root is", sqrt)

# Execute the function
main()


