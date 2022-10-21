# Complete the solve function below.
def solve(s):
    a = [l[0].upper() + l[1:] if len(l) > 0 else l.upper() for l in s.split(" ")]
    return " ".join(a)