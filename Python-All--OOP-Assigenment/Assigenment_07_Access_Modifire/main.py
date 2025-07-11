#--------Assigenment 07---------#
#Access Modeifires: Public, Private, Protected:
#Create a class Employe with:
# a public variable name,
# a private variable salary,
# a protected variable _ssn
# Try accessing all three variables from an object of the class and document what happend.

class Employee():
    def __init__(self, name, salary, ssn):
        self.name = name              # Public
        self._salary = salary         # Protected
        self.__ssn = ssn              # Private

if __name__ == "__main__":
    emp = Employee("Mehwish", 60000, "11-567-7788")
    
    print("Public_variable:", emp.name)
    print("Protected_variable:", emp._salary)
    print("Private_variable (via name mangling):", emp._Employee__ssn)

    try:
        print("Private_variable:", emp.__ssn)
    except AttributeError:
        print("Cannot access Private_variable __ssn directly.")




        