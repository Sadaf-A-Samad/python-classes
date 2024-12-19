from abc import ABC, abstractmethod

class MyAbstractPolygon(ABC):

    @abstractmethod
    def shapeSides(self, s):
        pass

class Triangle(MyAbstractPolygon): 
    def shapeSides(self, s, x = 8):
        print(f'My sides are {s}.')

class Square(MyAbstractPolygon):
    def shapeSides(self, s):
        print(f'My sides are {s}.')


t = Triangle()
t.shapeSides(3)

s = Square()
s.shapeSides(4)

