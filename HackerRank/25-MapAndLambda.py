cube = lambda x: x**3 

def fibonacci(n):
    ar =[]
    for i in range(n):
        if i==0:
            ar.append(0)
        elif i==1:
            ar.append(1)
        else:
            ar.append(ar[i-1]+ar[i-2])
    return ar