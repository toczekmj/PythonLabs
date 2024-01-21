# podpunkt A) 
# zdefiniować w ramach klasy A funkcję foo(self, x), metodę klasy class_foo, metodę statyczną static_foo, 
# tak, żeby kod poniżej drukował treści jak w komentarzach

class A(object):
    def foo(self, x):
        print("wykonanie foo(" + str(self) + ',' + str(x) + ')')

    @classmethod
    def class_foo(cls, x):
        print("class_foo(" + str(cls) + ',' + str(x) + ',')

    @staticmethod
    def static_foo(x):
        print("wykonanie static_foo(" + str(x) + ')')


a = A()
a.foo(123)  # wykonanie foo(<__main__.A object at 0x0000023A680D1F10>, 123)
A.foo(a, 123)  # ditto
a.class_foo(123)  # class_foo(<class '__main__.A'>, 123)
A.class_foo(123)  # ditto
a.static_foo(123)  # wykonanie static_foo(123)
A.static_foo(123)  # ditto

# podpunkt B)
# zdefiniować dowolną klasę bazową dziedzicząca z ABC i posiadającą metodę abstrakcyjną
# po czym zdefiniować ze dwie klasy potomne z odpowiednimi definicjami, zademonstrować w działaniu
from abc import ABC, abstractmethod


class Pojazd(ABC):
    @abstractmethod
    def wlejPaliwo(self):
        pass


class Bolid(Pojazd):
    def wlejPaliwo(self):
        print("wlewam paliwo E10")


class Samochod (Pojazd) :
    def wlejPaliwo(self):
        print("wlewam olej napędowy")


b = Bolid()
s = Samochod()
b.wlejPaliwo()
s.wlejPaliwo()

# podpunkt C)
# zdefiniować dowolną klasę oraz atrybut klasy tak, że stanie się on atrybutem czytanym poprzez 
# dekorator @property, a ustawianym za pomocą @nazwa.setter, pokazać w działaniu

class Klasa:
    def __init__(self):
        self.x = -999
        self._z = 0

    @property
    def cords(self):
        print("X: " + str(self.x))
        return self._z

    @cords.setter
    def cords(self, z):
        print("new X: " + str(z))
        self.x = z
        if z > self.x:
            print("X < Z")
        elif z < self.x:
            print("X > Z")
        else:
            print("X == Z")

        self._z = z


k = Klasa()
k.cords = 1
k.cords = 2
k.cords = 37
k.cords = 4
k.cords = 3
k.cords = 2
k.cords = 1
k.cords = 21
k.cords = 6

print(k.cords)
