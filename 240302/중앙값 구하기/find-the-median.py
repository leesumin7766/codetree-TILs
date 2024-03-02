inp = input()

arr = inp.split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

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