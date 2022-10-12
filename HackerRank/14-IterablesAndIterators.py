from itertools import combinations as comb

n = int(input())
s = input().split()
k = int(input())
l = list(comb(s, k))
j = [j for j in l if 'a' in j]
print(len(j)/len(l)) 