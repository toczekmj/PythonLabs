def fun(inp):
    binary = bin(int(inp))[2:].strip("0")
    max_len = 0
    current_len = 0

    for i in range(0, len(binary)):
        if binary[i] == '0':
            current_len += 1
        else:
            max_len = max(max_len, current_len)
            current_len = 0
    return max_len


inp = input("Podaj liczbę w postaci dziesietnej: ")
print(fun(inp))