'''
Code written by Parker F Sheley
Date 2/4/2024
Peogram Kattis Buka problem
Algorithm steps: 
input a number, A
input an operator 4
input second number, B
use eval() to evaluate the expression A operator B 
'''
a = input()
operator = input()
b = input()
expression = a+operator+b
print(eval(expression))