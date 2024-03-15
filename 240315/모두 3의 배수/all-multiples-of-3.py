n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

satisfied = True

for i in range (n1, n5 + 1):
    if i % 3 == 0 :
        satisfied = True

if satisfied == True :
    print("1")
else :
    print("0")