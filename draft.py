N = input("Enter the string: ")
temp = len(N)
for i in range(1, temp + 1):
    for x in range(0, temp - 1):
        print(N[x], end="")
    for y in range(0, x):
        print(" ", end="")
    temp -= 1
    print()