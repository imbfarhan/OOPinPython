class Computer:
    def config(self):
        print("hello")


com1 = Computer()

com1.config()
#Internally, com1.config() is interpreted as Computer.config(com1) , com1 is passed as a parameter
Computer.config(com1)