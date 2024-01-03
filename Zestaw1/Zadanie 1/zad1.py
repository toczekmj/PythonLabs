import sys

argv = sys.argv[1:]

for i in range(len(argv)):
    n = int(argv[i])
    print(str(n) + " ", end="")
    factor = ""
    k = 2
    while n > 1:
        count = 0
        while n % k == 0:
            count += 1
            n /= k
        if count > 1:
            factor += str(k) + "^" + str(count) + "*"
        elif count == 1:
            factor += str(k) + "*"
        k += 1
    print(factor[:-3])