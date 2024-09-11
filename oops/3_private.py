class Smartphone:
    def __init__(self):
        self.__model_name ="Android"
        print("Company model name",self.__model_name)
    def __display(self):
        print("This is smartphone")
        print(self.__model_name)

smart_obj =Smartphone()
print(smart_obj.__display())
smart_obj.__model_name="Iphone"
print("modified model name",smart_obj.__model_name)