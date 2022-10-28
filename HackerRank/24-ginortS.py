s = input()
lower = sorted([c for c in s if c.islower()])
upper = sorted([c for c in s if c.isupper()])
num = sorted([c for c in s if c.isnumeric()])
odd = sorted([c for c in num if int(c) % 2 == 1])
even = sorted([c for c in num if int(c) % 2 == 0])
print(''.join(lower) + ''.join(upper) + ''.join(odd) + ''.join(even))