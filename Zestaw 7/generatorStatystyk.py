import time
from mtablica import MonitorowanaTablica
from zad1 import bubble_sort
from zad2 import shell_sort
from zad3 import merge_sort
from zad4 import quick_sort
from zad5 import tim_sort
options = ["R", "S", "A", "T"]
N = 50
sorts = [
    ["Bubble sort", bubble_sort],
    ["Shell sort", shell_sort],
    ["Merge sort", merge_sort],
    ["Quick sort", quick_sort],
    ["Tim sort", tim_sort]
]

f = open("stats.txt", "w")

for s in sorts:

    f.write(f"{s[0]}\n")
    for typ in options:
        tablica = MonitorowanaTablica(0, 1000, N, typ)

        t0 = time.perf_counter()
        s[1](tablica)
        delta_t = time.perf_counter() - t0

        f.write(
            f"{typ}: Tablica posortowana w czasie {delta_t * 1000:.1f} ms. Liczba operacji: {len(tablica.pelne_kopie):.0f}.\n"
        )
    f.write("\n")
f.close()
