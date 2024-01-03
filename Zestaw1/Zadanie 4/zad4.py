import time

length = int(input("Podaj długość paska: "))

def display(n, p):
    zaladowane = int(n * p / 100)
    pozostale = n - zaladowane
    pasek = "|" + "=" * zaladowane + "-" * pozostale + "| " + str(p) + "%"
    print(pasek, end='\r')



for i in range(101):
    display(length, i)
    time.sleep(0.1)