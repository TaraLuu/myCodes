# Enter your code here. Read input from STDIN. Print output to STDOUT
score = 0
n, m = map(int,input().split())
x = list(input().split())
y = set(list(input().split()))
z = set(list(input().split()))
for i in x:
    if i in y: score += 1
    if i in z: score -= 1
print(score)