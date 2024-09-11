class Mathematics:
    def add (self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def mul(self,a,b,c=1):
        print(a*b*c)
class Calc(Mathematics):
    def add(self,a,b,c=0):
        print("Sum of two number is",a+b+c)
    def sub(self,a,b):
        print("Difference of two number is:",a-b)
    def mul(self,a,b,c=1):
        print("Product of numbers is:",a*b*c)
obj_1 =Calc()
obj_1.add(2,3,4)
obj_1.sub(3,2)
obj_1.mul(2,3,4)