def fun(x, y, z, n):
    return [[i, j, k]
            for i in range(x+1)
            for j in range(y+1)
            for k in range(z+1)
            if i + j + k != n]


x = input("X: ")
y = input("Y: ")
z = input("Z: ")
n = input("N: ")

print(fun(int(x), int(y), int(z), int(n)))