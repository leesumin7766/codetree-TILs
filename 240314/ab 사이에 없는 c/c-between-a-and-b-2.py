a ,b ,c = input().split()

a = int(a)
b = int(b)
c = int(c)
satisfied = True
for i in range(a, b + 1):
    if i % c == 0 :
        satisfied = False 
    
if satisfied == True :
    print("YES")
else :
    print("NO")