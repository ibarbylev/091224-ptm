class A:
    def method(self):
        print("A method")


class B(A):
    def method(self):
        print("B method")


class C(A):
    def method(self):
        print("C method")


class D(B, C):
    pass


obj = D()
obj.method()  # B method
print(D.__mro__)


