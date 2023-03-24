class A:

    def show(self):
        super().show()
        print("show from A")

class B:

    def show(self):
        print("show from B")

class C(A,B):

    def show(self):
        super().show()
        print("show from C")

c1=C()
c1.show()
