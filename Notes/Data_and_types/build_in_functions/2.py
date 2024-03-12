import math
import random
max_num = max(1,-2,33,5)
print(max_num)

print('2 to the 3rd power = ', pow(2,3))
print('2 to the 3rd power = ', 2**3)

print('hi', 'hello', end='=')
print('hi', 'hello', sep='', end='=')

num1 = 1
num2 = 4
num3 = -6
print(num1,num2,num3, sep='+', end="=")
print(num1+num2+num3)

import sys
line1a, line1b = input().split('|')
line2a, line2b = input().split('|')
print(line1a, line1b, file=sys.stderr) #use file=sys.stderr so kattis ignores output
print(line2a, line2b, file=sys.stderr)

first = line1a + line2a
second = line1b + line2b
print(first,second)

