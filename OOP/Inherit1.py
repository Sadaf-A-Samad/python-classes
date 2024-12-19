class p1:
    a = ''

    def __init__(self, myval):
        self.a = myval
        print(f"Hello I am init function. {myval}")

    def printMsg(self,a):
        self.a = a
        print(f"Hello I am Parent Class Function...{a}")

class c1(p1):
    pass

class c2(p1):
    a = 25

    def __init__(self, myval):
        self.a = myval
        print(f"Hello I am init from child. {myval}")
        super().__init__('I am super from Child2')

    def printMsg(self):
        super().printMsg(5)
        print("Hello I am Child Class Function...")
        


# child = c1('i am child')
child2 = c2(780)
c2.printMsg()
