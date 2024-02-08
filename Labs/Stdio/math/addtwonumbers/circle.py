##
# Circle - Basic Math - Homework
# Updated By: Parker Sheley
# Date: 2/8/2024
# CSCI 110
#
# This program prompts user to enter radius of a circle and calculates and displays area
# and circumference of the circle.
#
# Algorithm steps:
#	1. Prompt user to enter radius
#	2. Store radius into a variable
#	2. Calculate area using the formula: pi * radius * radius
#	3. Calculate circumference using the formula: 2 * pi * radius
#	4. Display the calculated values of area and circumference with proper description
###
# import math library that has PI and other functions defined
import math

print("This program finds and displays area and circumference of a circle given some radius.")
input('Enter to continue...')
# Step 1 and 2
radius = input("Enter radius of a circle: ")
radius = float(radius)  # convert string to float value

# Step 3
area = math.pi * radius**2  # * is product and ** is power operator in Python

# Step 4
# FIXED3:
# calculate and store the circumference into a variable
circumference = (2 * math.pi * radius)
# Display the calculated values with proper descriptions
print("Radius of the circle =",  radius)
print("area of the circle =", area)
print("Circumference =", circumference)
# FIXED4: display area

# FIXED5: display circumference

# Verify/Test your program if the calculated results are correct
# Run and test your program with different values for radius
print('Good bye...')