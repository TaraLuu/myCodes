# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
d = OrderedDict()
n = int(input())
for _ in range(n):
    item, price = input().rsplit(' ', 1)
    d[item] = d.get(item, 0) + int(price)

for key, value in d.items():
    print(key, value)