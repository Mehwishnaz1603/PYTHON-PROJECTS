#--------Assigenment 01---------#
#Using Self:
#Create a Class Student with attributes names and marks. Use the keyword to initilize this values via a constructor
#Add a method display() that prints students details.
 
class Student:
    def __init__(self, name, marks):
        self.name= name
        self.marks = marks

    def display (self):
            print (f"Name: {self.name}, Marks: {self.marks}")

if __name__ == "__main__":
    student1 = Student("Mehwish", 97)
    student1.display()                    # Output: Name: Mehwish, Marks: 97
    student2 = Student("Amna", 78) 
    student2.display()                    # Output: Name: Amna, Marks: 78


