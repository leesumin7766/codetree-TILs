n = int(input())

cnt = 'A'

for i in range(n) :
    for j in range(0,i +1) :
        print(cnt, end = "")
        cnt =chr(ord(cnt) + 1) 
        if cnt > 'Z' :
            cnt = 'A'
    print()