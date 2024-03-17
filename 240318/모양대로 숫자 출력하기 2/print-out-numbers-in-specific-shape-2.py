n = int(input())

cnt = 2

for i in range(n) :
    for j in range(2 , n + n + 1, 2) :
        print(cnt , end = " ")
        cnt += 2
        if cnt == 10 :
            cnt =2
    print()