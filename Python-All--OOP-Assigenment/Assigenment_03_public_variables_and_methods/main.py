#--------Assigenment 03---------#
#Public Vriables And Methods:
#Create a Class  Car witha public variable brand and a public method start(). 
# Instentiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):  # Fixed typo here
        self.brand = brand

    def start(self):
        print(f"The {self.brand} car is started.")

if __name__ == "__main__":  # Fixed typo here
    car1 = Car("Toyota")
    print(car1.brand)
    car1.start()
