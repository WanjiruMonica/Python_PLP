# A simple calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Type operator from the list (+, - , *, /): ")

if operator == '+':
    print(f"{a} + {b} = {a + b}")
          
elif operator == '-':
    print(f"{a} - {b} = {a - b}")

elif operator == '*':
    print(f"{a} * {b} = {a * b}")

elif operator == '/':
    print(f"{a} * {b} = {a * b}")

else:
    print("Invalid operator. Please use one of the following: +, -, *, /")


print("Thank you for using the calculator!")



          
          
