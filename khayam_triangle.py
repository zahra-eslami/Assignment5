from math import factorial

def khayam_triangle(x):
    for i in range(x):
        for j in range(x-i+1):
            print(end="  ")
        for j in range(i+1):
            cr = factorial(i) // (factorial(j) * factorial(i - j))
            print(cr, end="   ")
        print()

try:
    n = int(input("enter n: "))
    khayam_triangle(n) 
except ValueError:
    print("You must enter an integer number")
