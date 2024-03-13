a ,b ,c = input().split()

a = int(a)
b = int(b)
c = int(c)
satisfied = False
for i in range(a, b + 1):
    if i % c == 0 :
        satisfied = False 
    else :
        satisfied = True
if satisfied :
    print("YES")
else :
    print("NO")