class Teamaker:
    def __init__(self,sugar,tea_leaf,water):
        self.sugar =sugar
        self.tea_leaf =tea_leaf
        self.water =water        
        self.start()
    def start(self):
        self.gas_on()
        self.put_necessary_material()
        self.boil()
        self.gas_stop()

    def gas_on(self):
        print("congrats gas is on")
    def gas_stop(self):
        print("Gas is stopped")
    def put_necessary_material(self):
        print(f"Materials added to pot. sugar{self.sugar}chamcha,leaf{self.tea_leaf}chamcha,water{self.water}glass")
    def boil(self):
        print("water is boiling")

tea_maker_obj =Teamaker(3,2,5)



