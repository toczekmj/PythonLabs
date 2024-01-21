maxlvl = 0
maxlist = []


def find(lists, lvl):
    global maxlvl, maxlist
    for i in lists:
        if isinstance(i, list):
            find(i, lvl+1)
    if lvl > maxlvl:
        maxlvl = lvl
        maxlist = [lists]
    else:
        if lvl == maxlvl:
            maxlist.append(lists)


def insert(list):
    global maxlvl, maxlist
    maxlist = []
    maxlvl = 0
    find(list, 0)
    for i in maxlist:
        i.append(i[len(i) - 1] + 1)
    return list


lista = [1, [2, 3], 4]
print(insert(lista))
lista = [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]
print(insert(lista))
lista = [1, [3], [2]]
print(insert(lista))
lista = [1, 2, [3, 4, [5, 6], 5], 3, [4, 5]]
print(insert(lista))