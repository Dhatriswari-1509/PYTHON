n1 = int(input("enter a number1: "))
n2 = int(input("enter a number2: "))
operation = input("enter the operation:")
if operation == "+":
    print(n1 + n2)
elif operation == "-":
    print(n1 - n2)
elif operation == "*":
    print(n1 * n2)
elif operation == "//":
    print(n1 // n2)
elif operation == "%":
    print(n1 % n2)
else:
    print("Invalid operation")

