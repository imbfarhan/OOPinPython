class A:
    def f1(self):
        print("feature1")

class B(A):
    def f2(self):
        print("feature2")

a1=A()

a1.f1()

b1=B()

b1.f1()
b1.f2()
