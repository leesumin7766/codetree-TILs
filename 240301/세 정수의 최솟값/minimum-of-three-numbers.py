inp = input()
arr = inp.split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if a < b and a < c :
    print(a)
elif b < a and b < c :
    print(b)
elif c < b and c < a :
    print(c)
elif a < b and b == c :
    print(a)
elif b < a and a == c :
    print(b)
elif c < b and b == a :
    print(c)