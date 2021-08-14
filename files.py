from abc import ABC,abstractmethod
class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass
class Triangle(Polygon):
    def noofsides(self):              # method overriding
        print(" i have 3 sides")
class Pentagon(Polygon):
    def noofsides(self):              # method overriding
        print("i have 5 sides")
class Hexagaon(Polygon):
    def noofsides(self):              # method overriding
        print("i have 6 sides")
class Quadrilateral(Polygon):
    def noofsides(self):              # method overriding
        print("i have 4 sides")

r = Triangle()
r.noofsides()

k= Pentagon()
k.noofsides()

b = Quadrilateral()
b.noofsides()

c= Hexagaon()
c.noofsides()