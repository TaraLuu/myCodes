import re
for i in range(int(input())):
    s1 = input()
    s2 = re.sub(r"(?<= )(&&)(?= )", "and", s1)
    print(re.sub(r"(?<= )(\|\|)(?= )", "or", s2))