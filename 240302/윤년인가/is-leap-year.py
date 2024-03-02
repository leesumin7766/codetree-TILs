y = int(input())

if y % 4 == 0 :
    print("true")
    if y % 400 == 0:
        print("false")
else :
    print("false")