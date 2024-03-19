n = int(input())

cnt = 1

for i in range(n) :
    if i % 2 == 0 :
        for j in range(cnt , cnt + n ) :
            print(cnt , end = " ")
            cnt += 1
    else :
        for j in range(cnt + i , cnt  + i - n  , -1) :
            print(j + 1 , end = " ")
            cnt += 1

    print()