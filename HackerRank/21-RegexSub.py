import re
for _ in range(int(input())):
    s = input()
    s1 = re.sub(r"(?<= )(&&)(?= )", "and", s)
    print(re.sub(r"(?<= )(\|\|)(?= )", "or", s1))