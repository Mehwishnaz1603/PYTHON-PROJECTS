#--------Assigenment 06---------#
#Constructor And Destructor:
#Create a class logger that prints a message when an object is created (constructor) and another message when 
#it is destroyed destructor:

class Logger:
    def __int__(self):
        print("Logger object created")
        
    def __del__(self):
            print("Logger object destroyed")
if __name__ == "__main__":
    log = Logger()
    del log
