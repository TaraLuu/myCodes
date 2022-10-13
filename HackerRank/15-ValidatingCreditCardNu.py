import re
for i in range(int(input())):
    j=input()
    if (re.fullmatch(r"^[456]\d{3}(-?\d{4}){3}$", j) and \
    not re.search(r"([0-9])(-?\1){3}", j)):
        print("Valid")
    else:
        print("Invalid")