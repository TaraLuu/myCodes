# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = '.*\+'
t = int(input())
for _ in range(0,t):
    s = input()
    try:
        re.compile(s)
        result = 'True'
    except:
        result = 'False'
    print(result)