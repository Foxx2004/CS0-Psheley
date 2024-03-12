"""
HW - Loop

By: Parker Sheley

CSCI 110
Date: 3/10/2024


Algorithm steps:
1. Generates a number between 1 and 20 then sets it to r
2. Program greets user then askes them to input a number between 1 and 20
3. Program compares users number to r if too high says too high if too low says too low
4. asks 6 times if number is not == r then lose if user input == r user wind
5. in both win and lose cases askes if wants to play again if yes restarts program if no ends program
"""

import random
import sys
import os

def greet():
    name = input("Hello welcome to Guess the Number, what is your name? ")
    print("Nice to meet you "+ name)
    print("I am thinking of a number between 1 and 20")

def rN(min = 1, max = 20 ):
    r = random.randint(min,max)
    return r

def guess():
    print("You get 6 tries to guess the number. Take a guess:")
    r = rN()
    for _ in range(6):
        g = int(input())
        if g == r:
            print("you won!!!!!!!")
            playAgain()
        elif g > r:
            print("Your number is too big")
        elif g < r:
            print("Your number is too small")


    print("im sorry you lost the number was", r)
    playAgain()

def playAgain():
    choice = input("Would you like to play again N/Y ")
    if choice == 'N':
        sys.exit()
    elif choice == 'Y':
        os.system("cls")
        guess()
        
def main():
    greet()
    guess()

main()