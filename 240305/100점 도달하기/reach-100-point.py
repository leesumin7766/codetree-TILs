n = int(input())

for i in range (n , 101) :
    if i < 60 :
        print("F", end =' ')
    elif 70 > i > 59 :
        print("D", end =' ')
    elif 80 > i > 69 :
        print("C", end =' ')
    elif 90 > i > 79 :
        print("B", end =' ')
    else :
        print("A", end =' ')