#Ranabir
print("---------- Calculator -----------")



num1=float(input("Enter first number: "))
operation=input("Enter operation (+, -, *, /): ")
num2=float(input("Enter second number: "))

if operation == '+':
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")
elif operation == '-':
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")
elif operation == '*':
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")   

else:
    print("Invalid operation. Please enter one of the following: +, -, *, /.")        


# kousick
print("Hello world")