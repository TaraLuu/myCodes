import math

ab, bc = int(input()), int(input())
mbc = round(math.degrees(math.atan(ab/bc)))
print(f"{mbc}\N{DEGREE SIGN}")