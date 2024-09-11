def add(a,b,c=0):
    print(a+b+c)
add(2,3)
add(1,2,3)

#overiding

class Animal:
    def sound(self):
        print("this is animal sound")
class cat(Animal):
    def sound(self):
        print("mew mew ..")
cat_obj =cat()
cat_obj.sound()

class Mathematics:
    def add (self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def mul(self,a,b,c=1):
        print(a*b)
