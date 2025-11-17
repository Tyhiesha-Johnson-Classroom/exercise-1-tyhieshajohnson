# Question 1: Variable Assignment and String Manipulation

# Ask the user for their name and store it in a variable
name = input("What is your name? ")

# Ask the user for their age and store it in a variable
age = input("How old are you? ")

# Print a greeting using the name and age variables
print(f"Hello {name}, you are {age} years old!")

#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# Ask the user for the length of a rectangle and store it as an integer
length = int(input("Enter the length of the rectangle: "))

# Ask the user for the width of a rectangle and store it as an integer
width = int(input("Enter the width of the rectangle: "))

# Calculate the area of the rectangle
area = length * width

# Print the result
print(f"The area of the rectangle is {area} square units.")

#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# Ask the user for a temperature in Celsius and store it as a float
celsius = float(input("Enter temperature in Celsius: "))

# Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# Print the result rounded to two decimal places
print(f"The temperature in Fahrenheit is {fahrenheit:.2f}°F.")
