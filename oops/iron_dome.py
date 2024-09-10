#radar sense the eneny rocket and send to control system
#if enemy is detected control system processing and send signal to missile system 
# missile system launch rocket to enemy rocket where it should intercept.abs
import random
import time

class Airdefence:
    def __init__(self,enemy_rocket):
        self.enemy_rocket = enemy_rocket
        

    def radar(self):
        #it gives signal of enemy object ,True,angle,speed
        print("Warning!!!Enemy detected,Sending signal to control system")

    def control_system(self):
        angle = random.randint(1,361)
        speed =random .randint(1,1000)
        print(f"\n Enemy rocket is coming at {angle} degree")
        print(f"\n Enemy rocket is coming at {speed} km/h")

    def missile_system(self):
        print("\n Our missile rocket is activated to hit enemy's rocket.")
    


while True:
    time.sleep(2)
    enemy_rocket =random .choice([True,False])
    air_defence_obj =Airdefence(enemy_rocket)
    
    if enemy_rocket ==True:
        air_defence_obj.radar()
        random.randint(1,361)
        random .randint(1,361)
        air_defence_obj.control_system()
        air_defence_obj.missile_system()
    else:
        print("No enemy detected")
