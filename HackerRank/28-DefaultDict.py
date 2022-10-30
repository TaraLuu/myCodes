from collections import defaultdict
    
num_a, num_b = list(map(int, input().split()))
d = defaultdict(list)
    
for a in range(num_a):
    letter = input()
    d[letter].append(str(a + 1))
    
for b in range(num_b):
    letter = input() 
    print(" ".join(d[letter]) or "-1")