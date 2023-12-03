from colorama import Fore

def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or j == 1 or i == j:
                print(Fore.YELLOW + str(i * j), end="\t")
            else:
                print(Fore.WHITE+str(i * j), end="\t")
        print("\n")

try:
    n = int(input("enter n: "))
    multiplication_table(n) 
except ValueError:
    print("You must enter an integer number")

