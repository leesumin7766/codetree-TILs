n = int(input())

cnt = 1

for i in range(n) :
    if i % 2 == 0 :
        for j in range(cnt , cnt + 3) :
            print(j , end = " ")
            cnt += 1
    else :
        for j in range(cnt + i , cnt  + i - 3  , -1) :
            print(j + 1 , end = " ")
            cnt += 1

    print()