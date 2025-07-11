#--------Assigenment 10---------#
#Instance Methods:
# Create a Class Dog with instance variables name and breed. Add an Instance method bark() that prints a message 
# including the dogs name.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

my_dog = Dog("Tommy", "Golden Retriever")
my_dog.bark()
