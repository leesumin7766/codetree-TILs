a ,b ,c = input().split()

a = int(a)
b = int(b)
c = int(c)
satisfied = False
for i in range(a, b):
    if i % c == 0 or i == c:
        satisfied = True 
    else :
        satisfied = False
if satisfied :
    print("NO")
else :
    print("YES")