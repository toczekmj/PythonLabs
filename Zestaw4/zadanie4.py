from functools import singledispatch, singledispatchmethod


class Dodawanie:
    @singledispatchmethod
    def dodaj(self, arg):
        return "nieznane przeladnowanie"

    @dodaj.register(str)
    def _(self, arg1, arg2):
        return str(int(arg1) + int(arg2))

    @dodaj.register(int)
    def _(self, arg1, arg2):
        return arg1 + arg2

    @dodaj.register(list)
    def _(self, lista):
        wynik = 0
        for i in range(0, len(lista)):
            wynik += lista[i]
        return wynik


dodawanie = Dodawanie()
print(dodawanie.dodaj("1", "2"))
print(dodawanie.dodaj(1, 2))
print(dodawanie.dodaj([1, 2]))
print(dodawanie.dodaj({1, 2}))


@singledispatch
def pomnoz(arg):
    return "nieznane przeladnowanie"


@pomnoz.register
def _(arg1: str, arg2: str):
    return str(int(arg1) + int(arg2))


@pomnoz.register
def _(arg1: int, arg2: int):
    return arg1 + arg2


@pomnoz.register
def _(lista: list):
    wynik = 0
    for i in range(0, len(lista)):
        wynik += lista[i]
    return wynik


print(pomnoz("3", "2"))
print(pomnoz(3, 2))
print(pomnoz([3, 2]))
print(pomnoz({3, 2}))
