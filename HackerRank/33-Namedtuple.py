# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n, Input = int(input()), namedtuple('Input', input())
s = 0
for i in range(n):
    s = s + int(Input(*input().split()).MARKS)
print(round(s/n, 2))  