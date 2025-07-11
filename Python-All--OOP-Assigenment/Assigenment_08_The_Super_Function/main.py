#--------Assigenment 08---------#
#The Super() Function:
#Create a class Person with a constructors that sets the name. Inherit a class Teacher from it add a subject field
#and use super() to call the base class constructor.

# Base class
class Person:
    def __init__(self, name):
        self.name = name

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of the base class
        self.subject = subject

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")

if __name__ == "__main__":
  teacher = Teacher("Miss. Mehwish", "CS")
  teacher.display_info()
