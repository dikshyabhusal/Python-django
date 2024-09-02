class Calculator:
    def add(self,a,b):
        print("Sum is :",a+b)
    def subtract (self,a,b):
        print("Difference is:",a-b)
    def multiply (self,a,b):
        print("Multiplication is:",a*b)
    def divide(self,a,b):
        print("Division is:",a/b)

a= int(input("Enter first number:"))
b = int(input("Enter second number:"))

class_obj = Calculator()
class_obj.add(a,b)
class_obj.subtract(a,b)
class_obj.multiply(a,b)
class_obj.divide(a,b)
