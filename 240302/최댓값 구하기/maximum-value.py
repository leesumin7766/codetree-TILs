a , b , c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a > b and a > c :
    print(a)
elif b > a and b > c :
    print(b)
else : 
    if a == b and b > c or a == c and c > b :
        print(a)
    elif b == c and b > a :
        print(b)
    
print(c)