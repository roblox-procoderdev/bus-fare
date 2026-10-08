class Vehicle:
    def __init__(self,fare,seating_capacity):
        self.fare=fare
        self.seating_capacity=seating_capacity
    def display(self):
        print("bus fare: ",self.fare)
        print("bus seating capacity: ",self.seating_capacity)
class coach_bus(Vehicle):
    def __init__(self,fare,seating_capacity,engine,comfortability):
        self.engine=engine
        self.comfortability=comfortability
        Vehicle.__init__(self,fare,seating_capacity)
bus=coach_bus(7500,75,'6 cylinder diesel',9.5)
bus.display()
print('engine: ',bus.engine)
print('comfortability: 9.5')