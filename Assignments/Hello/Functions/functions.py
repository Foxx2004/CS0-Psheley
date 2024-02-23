"""
Lab - Conditional Statements
By: Parker Sheley 
CSCI 110
Date: 2/22/2024
Program prompts user to enter a number and determines whether the entered number is even or odd, positive or negative or zero.
algorithim steps 
1. take 2 numbers from user 
2. put 2 numbers in many functions that add, subtract, multiply, devide, find the remainder, puts to the power of other number and square root each number
3. Display results with descriptions
4. run all test cases if pass says all test cases pass
"""
import math

def addTwo(A,B):
    sum = float(A + B)
    
    return sum
# adds number 1 and number 2 returns product 

def multTwo(A,B):
    sum = float(A * B)
    return sum
# multiplies number 1 with number 2 returns product

def devTwo(A,B):
    sum = float(A / B)
    return sum
#devides number 1 by number 2 then returns product

def minusTwo(A,B):
    sum = float(B - A)
    return sum
#subtracts number 2 from number 1 and returns difference 

def remainderTwo(A,B):
    sum = float(A % B)
    return sum
#finds the remainder of number1 one devided by number 2 and reyturns remainder

def powerTwo(A,B):
    sum = float(A ** B)
    return sum
# puts number 1 to the power of number 2 then returns result

def squrtOne(A):
    sum = math.sqrt(A)
    return sum
#takes square root of number 1 and returns the sum

def squrtTwo(B):
    sum = math.sqrt(B)
    return sum
#takes square root of number 2 and returns the sum

def test():
    assert addTwo(3,4)== 7
    assert addTwo(2,2)==4
    assert multTwo(2,2)==4
    assert multTwo(2,3)==6
    assert devTwo(2,2)==1
    assert devTwo(100,2)==50
    assert minusTwo(2,2)==0
    assert minusTwo(4,7)==3
    assert remainderTwo(7,4)==3
    assert remainderTwo(6,4)==2
    assert powerTwo(2,2)==4
    assert powerTwo(2,3)==8
    assert squrtOne(1)==1
    assert squrtOne(4)==2
    assert squrtTwo(1)==1
    assert squrtTwo(4)==2
    
    print("all test cases pass")
#Tests all functions twice and if all correct prints "all test cases pass"

def main():

    A = float(input("Enter 1st Number "))
    B = float(input("Enter 2nd Number "))
    print("your numbers added together = ",addTwo(A,B))
    print("your numbers multiplied together = ",multTwo(A,B))
    print("number 1 devided by number 2 = ",devTwo(A,B))
    print("number 2 minus number 1 = ",minusTwo(A,B))
    print("The remainder of number 1 and number 2 = ",remainderTwo(A,B))
    print("number 1 to the power of number 2 = ",powerTwo(A,B))
    print("the squareroot of number 1 = ",squrtOne(A))
    print("the squareroot of number 2 = ",squrtTwo(B))

# takes 2 numbers from user then displays numbers with certain alterations defined by funtions then deisplays with proper discriptions 
main()
test()
#calls test and main functions