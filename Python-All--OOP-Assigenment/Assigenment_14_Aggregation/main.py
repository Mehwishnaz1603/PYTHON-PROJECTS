#--------Assigenment 14---------#
#Aggregation:
#Create a class Department and a class Employee. Use aggregation by having a Department object stores a reference to an
#Employee object that exists independtly of it.

# Employee class
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Employee Name: {self.name}, ID: {self.emp_id}")

# Department class using aggregation
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee              # Aggregation: Department "has" an Employee

    def show_department_info(self):
        print(f"Department: {self.dept_name}")
        self.employee.display_info()          # Access Employee's method
if __name__ == "__main__":
   emp = Employee("Alice", 101)               # Employee exists independently
   dept = Department("HR", emp)
   dept.show_department_info()
