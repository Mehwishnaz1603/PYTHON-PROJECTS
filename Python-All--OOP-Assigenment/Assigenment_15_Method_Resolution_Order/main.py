#--------Assigenment 15---------#
# Method Resolution Order (MRO):
# Create four classes:
#     A with a method show(),
#     B and C that inherit from A and override show(),
#     D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("Method from class A")

class B(A):
    def show(self):
        print("Method from class B")

class C(A):
    def show(self):
        print("Method from class C")


class D(B, C):
    pass
d = D()
d.show()

print(D.mro())