"""
Written: by Parker Sheley
Date: 2\14\2024

This code will take 3 sides from the user and will calculate the area and perimeter of the given triangle
"""
import math

greet = input("Hello what is your name? ")
print("welcome "+ greet)
#takes user name and greets them #
A = int(input("how long is the first side "))
B = int(input("how long is the first second side "))
C = int(input("how long is the first third side "))
#Takes user input and coverts to integers #

Peremeter = A + B + C
D = (Peremeter/2)
Area = (math.sqrt(D*(D-A)*(D-B)*(D-C)))
#calculates area and peremeter from user imput using Herons formula#
print ("The area of the given triangle is ",Area)
print ("The peremeter of the given triangle is ",Peremeter)
#displays calculated values#