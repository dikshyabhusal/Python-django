class Smartphone:
    def __init__(self):
        self.model_name ="Android"
        print("Company model name",self.model_name)


smart_obj =Smartphone()

smart_obj.model_name="Iphone"
print("modified model name",smart_obj.model_name)