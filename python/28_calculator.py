def add(a,b):
    print(a + b)
def subtract(a,b):
    print(a - b)
def multiply(a,b):
    print(a * b)
def divide(a,b):
    print(a / b)
def modulus(a,b):
    print(a % b)


a= int (input("Enter first number"))
operator = input("Enter operator")
b = int(input("Enter second number"))

if operator == '+':
    add(a,b)
elif operator == '-':
    subtract(a,b)
elif operator == '*':
    multiply(a,b)
elif operator == '/':
    divide(a,b)
elif operator =='%':
    modulus(a,b)
else:
    print("Invalid operator")



