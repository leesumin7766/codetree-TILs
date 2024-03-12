n = int(input())

satisfied = False
if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 :
    satisfied = True

if satisfied == True :
    print('C')
else :
    print('N')