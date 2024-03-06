"""
HW - Conditionals

By: Parker Sheley 

CSCI 110
Date: 3/1/2024 

Program prompts user to enter a number and determines whether the entered number is even or odd, positive or negative or zero.

Algorithm steps: 
1: Takes 5 numbers from user 
2: Converts numbers to int then adds them, finds the product, the avg and the smallest/biggest number entered 
3: Prints results
4: Asks user if they would like to repeat proccess

"""
import os

def numplus5(num1, num2, num3, num4, num5):
    ans = (num1+num2+num3+num4+num5)
    return ans

def nummult5(num1, num2, num3, num4, num5):
    (num1, num2, num3, num4, num5)
    ans = (num1*num2*num3*num4*num5)
    return ans

def numavg5(num1, num2, num3, num4, num5):
    ans = (numplus5(num1, num2, num3, num4, num5)/5)
    return ans

def nummax5(num1, num2, num3, num4, num5):
    L1 = [num1, num2, num3, num4, num5]
    L1.sort()
    return (L1[-1])

def nummin5(num1, num2, num3, num4, num5):
    L1 = [num1, num2, num3, num4, num5]
    L1.sort()
    return (L1[0])

def main():
    num1 = int(input("input 1st number "))
    num2 = int(input("input 2nd number "))
    num3 = int(input("input 3rd number "))
    num4 = int(input("input 4th number "))
    num5 = int(input("input 5th number "))
    print("The biggest number you entered is: ",nummax5(num1, num2, num3, num4, num5))
    print("The smallest number you entered is: ",nummin5(num1, num2, num3, num4, num5))
    print("The product of your numbers is: ",nummult5(num1, num2, num3, num4, num5))
    print("Your numbers added together is equal to: ",numplus5(num1, num2, num3, num4, num5))
    print("The average of your numbers is: ",numavg5(num1, num2, num3, num4, num5))
    restart()

def restart():
    while True:
        choice = input("Would you like to enter 5 more numbers: Y/N ")
        if choice in ['Y','N']: 
            break
    if choice == 'Y':
             os.system('cls')
             main()
    else:
         print("Goodbye")

def test():
     assert nummin5(2,5,7,8,99) == 2
     assert nummin5(2,5,1,8,99) == 1
     assert nummax5(2,5,7,8,99) == 99
     assert nummax5(2,5,76,8,9) == 76
     assert numplus5(5,5,5,5,5) == 25
     assert numplus5(5,5,5,5,6) == 26
     assert nummult5(5,5,5,5,5) == 3125
     assert nummult5(2,2,2,2,2) == 32
     assert numavg5(5,5,5,5,5) == 5
     assert numavg5(2,2,2,2,2) == 2
test()
main()