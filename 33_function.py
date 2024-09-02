def addition(a,b):
    return int(a)+int(b)
def subtraction (a,b):
    return int(a)-int(b)
def multiply (a,b):
    return int(a)*int(b)
def divide (a,b):
    return int(a)/int(b)


first_number=input("Enter first number:")
operator =input("Enter operator:")
second_number = input("Enter second number:")
if operator == '+':
    output = addition(first_number,second_number)
elif operator =='-':
    output = subtraction(first_number,second_number)
elif operator =='*':
    output = multiply(first_number,second_number)
elif operator =='/':
    output = divide(first_number,second_number)
else:
    print("Invalid operator")
print(output)
