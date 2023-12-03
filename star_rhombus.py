def star_rhombus(n):
    for i in range(n+1):
        print(" " * (n - i), end="")
        print("* " * i)

    for i in range(n-1,0,-1):
        print(" " * (n - i), end="")
        print("* " * i)

try:
    n = int(input("Enter the size of rhombus : "))
    star_rhombus(n)
except ValueError:
    print("Please enter an integer number")
