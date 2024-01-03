miarka="|"
dlugosc_segmentu = 5
liczby = "0"
nastepna_liczba = 1
segment = "....|"

ilosc = int(input("Podaj dlugosc miarki: "))

for i in range(ilosc):
    miarka += segment
    liczby += " " * (dlugosc_segmentu - len(str(nastepna_liczba))) + str(nastepna_liczba)
    nastepna_liczba += 1
print(miarka + "\n" + liczby)