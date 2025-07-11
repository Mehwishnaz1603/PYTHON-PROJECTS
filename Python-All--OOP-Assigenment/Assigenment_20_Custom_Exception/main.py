#--------Assigenment 20---------#
#Custom Exception:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if 
# age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older."):
        super().__init__(self.message)


def check_age(age):
    if age < 18:
        raise IndentationError(f"Invalid age: {age}. You must be at least 18 years old.")
    else:
        print("Age is valid.")

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except IndentationError as e:
    print(f"Error: {e}")
except ValueError:
    print("Please enter a valid number for age.")
