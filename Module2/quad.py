# Author: Kyle Freidhof
# Created: May, 25 2024
# LICENSE: MIT
# Credits: https://www.programiz.com/python-programming/examples/quadratic-roots
# About: A Program to solve quadratic equations

# import the cmath module
import cmath

# define the function quad
def quad():
    # ask for 3 inputs and store them in the varriable
    x = eval(input("Enter a number: "))
    y = eval(input("Enter a second number: "))
    z = eval(input("Enter a third number: "))

    # Solve the discriminant
    a = (y**2) - (4*x*z)

   # Find the two solutions
    sol1 = (-y + cmath.sqrt(a)) / (2*x)
    sol2 = (-y - cmath.sqrt(a)) / (2*x)
# Print the results 
# I had to fix this a bit compared to the original code
# I used the f string and seperated it into brackets
    print(f"The Answer is: {sol1} and {sol2}")

quad()

