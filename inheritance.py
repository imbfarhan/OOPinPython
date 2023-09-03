class A:
    def f1(self):
        print("feature1")


#Single inheritance
class B(A):
    def f2(self):
        print("feature2")

class C:
    def f3(self):
        print("feature3")

#Multiple inheritance
class D(A,C):
    def f4(self):
        print("feature3")

a1=A()

a1.f1()

b1=B()

b1.f1()
b1.f2()

d1=D()
d1.f3()
d1.f4()
d1.f1()