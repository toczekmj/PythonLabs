import numpy as np
import matplotlib.pyplot as plt


def printgraph(wielomian, x_min, x_max):
    x = np.linspace(x_min, x_max, 200)
    y = eval(wielomian, {"x": x, "np": np})

    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Wykres wielomianu")
    plt.grid(True)
    plt.show()

printgraph('5*x**4 + 2*x**3 - x + 6', -10, 10)