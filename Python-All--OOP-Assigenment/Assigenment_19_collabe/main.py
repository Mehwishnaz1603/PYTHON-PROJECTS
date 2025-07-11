#--------Assigenment 19---------#
#Collable() and __call__():
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an 
# input by the factor. Test it with callable() and by calling the object like a function.

# Define the class Multiplier
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Create an instance of Multiplier
double = Multiplier(2)

# Test if the object is callable
print(callable(double))  # Output: True

# Use the object like a function
result = double(20)  # Equivalent to 20 * 2
print(f"Result of double(10): {result}")
