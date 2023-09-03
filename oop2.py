class Computer:
    def __init__(self):
        self.name="Hello"
        self.age=28
    def update(self):
        self.age=30

c1 = Computer()
c2=Computer()

print(c1.age)
#Will print 28

c1.update()
#Now, how will update know which object's update is called? That will be done with the help of self.

print(c1.age)
#Will print 30