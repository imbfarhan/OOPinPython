class Student:
    def __init__(self,name):
        self.name=name
        self.lap=self.Laptop()
    
    class Laptop:
        def __init__(self):
            self.brand="HP"



s1=Student("Roy")

lap1=Student.Laptop()
print(lap1.brand)
print(s1.lap.brand)