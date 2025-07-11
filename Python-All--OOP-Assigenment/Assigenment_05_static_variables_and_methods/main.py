#--------Assigenment 05---------#
#Static Vriables And Static Methods:
#Create a class MathUtils with a static method add (a,b) that returns the sum. No class or instance variable should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

if __name__ == "__main__":
    result = MathUtils.add(5, 7)
    print("Sum:", result)  # Output: Sum: 12
