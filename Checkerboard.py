import numpy as np

def checkerboard(n, m):
    checklist = np.empty((n, m), dtype=object)
    for i in range(n):
        for j in range(m):
            if j % 2 == 0:
                checklist[i, j] = "∎"
            else:
                checklist[i, j] = "☐"
    return checklist

try:
    n = int(input("enter n: "))
    m = int(input("enter m: "))
    my_list = checkerboard(n, m)
    # for i in my_list:
    #     print(i)
    for i in range(n):
        for j in range(m): 
            print(my_list[i][j],end="")
        print()

except ValueError:
    print("You must enter an integer number")
