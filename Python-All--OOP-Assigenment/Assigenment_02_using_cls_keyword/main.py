#--------Assigenment 02---------#
#Using Cls:
#Create a Class  Counter that keeps track of how many objects have been created. Use a class variable and a classmethods 
# with cls to manage and display the count

class Counter:
    count = 0
    def __init__(self):
        Counter.count +=1
    @classmethod
    def show_count(cls):
        print(f" Total objects created: {cls.count}")
if __name__ == "__main__":
    object1 = Counter()
    object2 = Counter()
    object3 = Counter()
    Counter.show_count()
    
