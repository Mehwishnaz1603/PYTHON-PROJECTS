#--------Assigenment 13---------#
#Composition:
#Create a class Engine and create a class Car. Use composition by passing an Engine object to the Car class during initalization
# Access a method of the Engine class via the Car calss.

# Engine class
class Engine:
    def start(self):
        print("Engine started.")

# Car class using composition
class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car "has-a" Engine

    def start_car(self):
        print("Starting the car...")
        self.engine.start()  # Accessing Engine's method via Car

if __name__ == "__main__":
    engine_obj = Engine()
    my_car = Car(engine_obj)
    my_car.start_car()