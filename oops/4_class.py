class Mathematics:
    def _sum(self,a,b):
        print("Sum of two number",a+b)
    def __sum(self,a,b):
        print("protected",a+b)

obj_1 = Mathematics()
obj_1._sum(5,6)
obj_1.__sum(1,2)
