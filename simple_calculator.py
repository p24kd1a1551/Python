#python  program to implement simple calculator
a,b = [int(x) for x in input("1st value and 2nd value : ").split()]
print("""    For addition enter '+'\n
    For subtraction enter '-'\n 
    For Multiplication enter '*'\n
    For Division enter '/'\n""")
choice = input("Enter the operator :")
if choice == "+" :
    print(f"{a} + {b} = {a+b}")
elif choice == "-" :
    print(f"{a} - {b} = {a-b}")
elif choice == "*" :
    print(f"{a} * {b} = {a*b}")
elif choice == "/" :
    print(f"{a} / {b} = {a/b}")
else :
    print("Invalid operator ")
