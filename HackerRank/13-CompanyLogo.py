if __name__ == '__main__':
    s = list(input())
d = {}
for c in set(s):
    d[c]=s.count(c)
for k, v in sorted(d.items(), key=lambda x: (-x[1], x[0]))[0:3]:
    print(k, v)