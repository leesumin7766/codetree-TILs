n = int(input())

satisfied = True

if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 11 == 0 or n % 13 == 0:
     satisfied = False
     print("P")
else :
    satisfied = True
    print("C")