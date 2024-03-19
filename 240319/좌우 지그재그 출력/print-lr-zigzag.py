n = int(input())

cnt = 0

for i in range(n) :
    if i % 2 == 0 :
        for j in range(cnt , cnt + 3) :
            print(j + 1, end = " ")
            cnt += 1
    else :
        for j in range(cnt + 2, cnt -1  , -1) :
            print(j + 1, end = " ")
            cnt += 1

    print()