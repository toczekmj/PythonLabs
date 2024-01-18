#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split(' ')
    n = int(nm[0])
    m = int(nm[1])
    arr = []

    for i in range(n):
        arr.append(
            [int(arr_temp) for arr_temp in input().strip().split(' ')]
        )

    k = int(input().strip())
    sort = sorted(arr, key=lambda x: x[k])
    for i in sort:
        print(' '.join(str(y) for y in i))
