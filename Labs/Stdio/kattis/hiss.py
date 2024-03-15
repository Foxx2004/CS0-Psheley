'''
Name: Parker Sheley 
Date: 3/14/2024 
Program Description: Kattis problem bijele:
https://open.kattis.com/problems/hissingmicrophone
Algorithm Steps:
1. takes user input
2. checks if input conatins 'ss'
3. says hiss if double s is present says no hiss if it is not
'''

def hiss(phrase):
    if 'ss' in phrase:
        return True
    else:
        return False
     
def main():
    phrase = input()
    hiss(phrase)
    if hiss(phrase) == True: 
        print("hiss")
    else:
        print("no hiss")
main()