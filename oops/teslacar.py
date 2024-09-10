#an auto driving car 
#can detect object
#can decide itself where to move
#can set destinction location.
#implement battery in the car
#automatic charge

class Battery:
    def __init__(self):
        self.battery_percentage =50
        self.is_solar_charging =False

    def show_battery_percentage(self):
        return self.battery_percentage

    def solar_charge(self):
        self.is_solar_charging = True
        print("Car is charging with solar power..")

    def stop_solar_charge(self):
        self.is_solar_charging = False
        print("Solar charging stopped.")

    def charge(self):
        if self.battery_percentage < 100:
            self.battery_percentage += 10  
            print(f"Battery charged to {self.battery_percentage}%")
        else:
            print("Battery is fully charged!")

class ObjectDetect:

    def object_detect_detail(self):
        from random import choice
        return choice ([True,False])


class Tesla(Battery,ObjectDetect):
    def __init__(self):
        super().__init__() 
        self.is_moving = False
        self.is_stopped = True


    def stop(self):
        print("car is stop")
        self.is_stopped = True
        self.is_moving = False

    def move(self):
        
        battery_percentage =self.show_battery_percentage()
        if self.show_battery_percentage()  > 2:
            self.solar_charge()
            self.is_moving = True
            self.is_stopped = False
            print("Car is moving")
            if self.object_detect_detail() == True:
                print("Objects detected..")
                self.stop()
            else:
                print("Continue to move")
        else:
            print(" Battery low")
        print(f"Battery percentage: {self.show_battery_percentage()}%")

    def automatic_charge(self):
        while self.show_battery_percentage() < 100:
            self.charge()
        self.stop_solar_charge()

tesla_obj = Tesla()
tesla_obj.move()
tesla_obj.automatic_charge()
tesla_obj.move()

