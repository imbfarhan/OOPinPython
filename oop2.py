class Computer:
    def __init__(self):
        self.name="Hello"
        self.age=28
    def update(self):
        self.age=30
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False


c1 = Computer()
c1.age=44
c2=Computer()

print(c1.age)
#Will print 28

if(c1.compare(c2)):
    #c1 becomes self and c2 becomes other
    #c1 becomes self since c1 is calling it
    print("They are same")
else:
    print("They are different")

c1.update()
#Now, how will update know which object's update is called? That will be done with the help of self.
#Current instance is passed

print(c1.age)
#Will print 30