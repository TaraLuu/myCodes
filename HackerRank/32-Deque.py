# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
for _ in range(int(input())):
    o, *v = input().split()
    getattr(d, o)(*v)  
print(*d, sep=' ')