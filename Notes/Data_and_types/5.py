import math

def main():
    print("Hello World")
    A = calc_area(1)
    print(A)
    greet("Parker")

def greet(name):
    print(f"Hello {name}!")

def calc_area(radius):
    area = math.pi * radius**2
    return area

def find_max(a, b, c):
    if(a >= b and a >= c):
        return a
    if(b > a and b > c):
        return b
    if(c > b and c > a):
        return c

main()
