import re
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

matrix = list(zip(*matrix))


s = ' '.join(
        ''.join(
            p for c in matrix for p in c
        )
    .split()
)

print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', s))



