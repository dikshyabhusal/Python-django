number1=int(input("Enter first number = "))
operator=input("Enter operator:")
number2=int(input("Enter second number = "))

if operator =='+':
    print(number1 + number2)
elif operator=='-':
    print(number1 - number2)
elif operator=='*':
    print(number1 * number2)
elif operator=='/':
    print(number1 / number2)
elif operator =='%':
    print(number1 % number2)
else:
    print("Invalid operator")
