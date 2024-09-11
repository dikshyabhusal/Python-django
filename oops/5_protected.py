class Phone:
    def __init__(self):
        self._brandname ="Apple"
class Smartphone(Phone):
    def __init__(self):
        self._model_name ="Android"
        print("Company model name",self._model_name)
        super().__init__()

    def display(self):
        print("This is smartphone")
        print(self._brandname)
        print(self._model_name)

smart_obj =Smartphone()
smart_obj.display()
#print("modified model name",smart_obj._model_name)

