# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
lower = ""
upper = ""
even = ""
odd = ""

for c in s:
    if c.islower():
        lower += c
    elif c.isupper():
        upper += c
    elif c.isdigit():
        if int(c) % 2 == 0:
            even += c
        else:
            odd += c

print(''.join(sorted(lower) + sorted(upper) + sorted(odd) + sorted(even)))



