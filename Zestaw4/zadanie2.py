from math import hypot, atan, sin, cos, sqrt


class Zespolona:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def conjugate(self):
        return self.__class__(self.r, -self.i)

    def argz(self):
        return atan(self.i / self.r)

    def __abs__(self):
        return Zespolona(sqrt(pow(self.r, 2) + pow(self.i, 2)))

    def __repr__(self):
        return "Zespolona(" + str(self.r) + ", " + str(self.i) + ")"

    def __str__(self):
        return "(" + str(self.r) + ("+" if self.i > 0 else "") + str(self.i) + "j)"

    def __add__(self, other):
        (t_r, t_i) = (self.r, self.i)
        if isinstance(other, Zespolona):
            t_r += other.r
            t_i += other.i
        else:
            t_r += other
        return Zespolona(t_r, t_i)

    def __sub__(self, other):
        (t_r, t_i) = (self.r, self.i)
        if isinstance(other, Zespolona):
            t_r -= other.r
            t_i -= other.i
        else:
            t_r -= other
        return Zespolona(t_r, t_i)

    def __mul__(self, other):
        (t_r, t_i) = (self.r, self.i)
        if isinstance(other, Zespolona):
            new_r = t_r * other.r - t_i * other.i
            new_i = t_r * other.i + t_i * other.r
            return Zespolona(new_r, new_i)
        else:
            t_r *= other
            t_i *= other
        return Zespolona(t_r, t_i)

    def __radd__(self, other):
        (t_r, t_i) = (self.r, self.i)
        if isinstance(other, Zespolona):
            t_r += other.r
            t_i += other.i
        else:
            t_r += other
        return Zespolona(t_r, t_i)

    def __rmul__(self, other):
        (t_r, t_i) = (self.r, self.i)
        if isinstance(other, Zespolona):
            new_r = t_r * other.r - t_i * other.i
            new_i = t_r * other.i + t_i * other.r
            return Zespolona(new_r, new_i)
        else:
            return Zespolona(t_r * other, t_i * other)

    def __rsub__(self, other):
        t_r = self.r
        t_i = self.i
        if isinstance(other, Zespolona):
            other.r -= t_r
            other.i -= t_i
        else:
            return Zespolona(other - t_r, -t_i)
        return Zespolona(t_r, t_i)

    def __eq__(self, other):
        if not isinstance(other, Zespolona):
            return False
        return self.r == other.r and self.i == other.i

    def __ne__(self, other):
        return not self.__eq__(other)


    def __pow__(self, other):
        wynik = self

        for i in range(other - 1):
            wynik *= self
        return wynik

def main():
    print("Liczby zespolone")
    a = Zespolona(2, 5)
    b = Zespolona(1, -3)
    print(a)
    print(b)
    b_copy = eval(repr(b))
    print(type(b_copy), b_copy.r, b_copy.i)
    print(a + b)
    print(a - b)
    print(a + 4)
    print(7 - a)
    print(a * 4)
    print(a * (-4))
    print(a == Zespolona(2, 5))
    print(a == b)
    print(a != b)
    print(a != Zespolona(2, 5))
    print(a ** 2)
    print(b ** 4)


if __name__ == "__main__":
    main()

# Liczby zespolone
# (2+5j)
# (1-3j)
# <class '__main__.Zespolona'> 1 -3
# (3+2j)
# (1+8j)
# (6+5j)
# (5-5j)
# (8+20j)
# (-8-20j)
# True
# False
# True
# False
# (-21+20j)
# (28+96j)
