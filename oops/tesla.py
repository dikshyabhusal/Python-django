class Battery:
    def __init__(self):
        self.battery_percentage = 49  # Initial battery percentage
        self.is_solar_charging = False

    def show_battery_percentage(self):
        return self.battery_percentage

    def solar_charge(self):
        self.is_solar_charging = True
        print("Car is charging using solar power...")

    def stop_solar_charge(self):
        self.is_solar_charging = False
        print("Solar charging stopped.")

    def charge(self):
        if self.battery_percentage < 100:
            self.battery_percentage += 10  # Charge by 10% increments
            print(f"Battery charged to {self.battery_percentage}%")
        else:
            print("Battery is fully charged!")


class ObjectDetect:
    def object_detect_detail(self):
        # In real-world scenarios, this would detect actual obstacles
        # Randomly simulating object detection
        from random import choice
        return choice([True, False])


class Tesla(Battery, ObjectDetect):
    def __init__(self):
        super().__init__()  # Initialize Battery
        self.is_moving = False
        self.is_stopped = True

    def stop(self):
        print("Car is stopping...")
        self.is_stopped = True
        self.is_moving = False

    def move(self):
        battery_percentage = self.show_battery_percentage()

        if battery_percentage > 2:
            self.solar_charge()  # Charge using solar energy while moving
            self.is_moving = True
            self.is_stopped = False
            print("Car is moving...")

            if self.object_detect_detail():
                print("Object detected ahead!")
                self.stop()
            else:
                print("No objects detected. Continuing to move.")
        else:
            print("Battery is low. Please charge the car.")

        print(f"Battery percentage: {self.show_battery_percentage()}%")

    def automatic_charge(self):
        while self.show_battery_percentage() < 100:
            self.charge()
        self.stop_solar_charge()

# Testing the Tesla class
tesla_obj = Tesla()

# Trying to move the car
tesla_obj.move()

# Attempting automatic charge if needed
tesla_obj.automatic_charge()

# Move again after charging
tesla_obj.move()
