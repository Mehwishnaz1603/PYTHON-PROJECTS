#--------Assigenment 21---------#
# Custom Class Iterable:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make 
# the object iterable in a for-loop, counting down to 0.
class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        # The iterator returns itself
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1
            return value

# Example usage:
for number in Countdown(5):
    print(number)
