class Computer:
    def __init__(self,cpu,ram):
        #Constructor
        self.cpu=cpu
        self.ram=ram
    # def config(self):
    #     print("hello")
    def show(self):
        print("Config is "+self.cpu +" "+self.ram)


com1 = Computer("i5","16GB")
#com1 is passed automatically 
com2 = Computer("i7","32GB")

com1.show()
com2.show()

# com1.config()
# #Internally, com1.config() is interpreted as Computer.config(com1) , com1 is passed as a parameter
# Computer.config(com1)