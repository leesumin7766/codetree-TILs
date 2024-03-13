a ,b ,c = input().split()

a = int(a)
b = int(b)
c = int(c)
satisfied = False
for i in range(a, b):
    if i % c == 0 :
        satisfied = True 
    else :
        satisfied = False
if satisfied == True :
    print("NO")
else :
    print("YES")