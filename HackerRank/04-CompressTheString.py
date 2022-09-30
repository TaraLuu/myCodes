from itertools import groupby
[print((list(g).count(k),int(k)), end=" ") for k, g in groupby(input())]