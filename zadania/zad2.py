def odwracanie(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

def odwracanie_rek(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rek(L, left + 1, right - 1)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odwracanie(lista, 2, 6)
print(lista)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odwracanie_rek(lista, 2, 6)
print(lista)