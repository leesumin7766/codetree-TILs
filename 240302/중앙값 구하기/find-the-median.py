inp = input()

arr = inp.split()
a = arr[0]
b = arr[1]
c = arr[2]

if a > b  :
    if b >= c :
        print( b )
    elif b < c :
        if a >= c :
            print(c)
        else :
            print(a)

else :
    if a >= c :
        print(a)
    else :
        if b < c :
            print(b)
        else :
            print(c)