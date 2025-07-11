#--------Assigenment 04---------#
#Class Vriables And Class Methods:
#Create a Class  Car witha public variable brand and a public method start(). 
# Instentiate the class and access both from outside the class.

class Bank():
    bank_name = "ABC"
    @classmethod
    def change_bank_name (clas, name):
        clas.bank_name = name

if __name__ =="__main__":
    user1 = Bank()
    user2 = Bank()
    print("Before changing bank name:")
    print(user1.bank_name)
    print(user2.bank_name)

    Bank.change_bank_name("XYZ")
    print("After changing bank name:")
    print(Bank.bank_name)         # Output: XYZ


