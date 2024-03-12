a , b = input().split()
a = int(a)
b = int(b)
satisfied = False

for i in range(a, b + 1) :
    if i == 1 or i == 2 or i == 3 or i == 5 or i == 10 or i == 960 or i == 480 or i == 240 or i == 120 or i == 60 or i == 30 or i == 15 or i ==14 or i ==12 or i == 10 :
        satisfied = True
if satisfied == True :
    print("1")
else :
    print("0")