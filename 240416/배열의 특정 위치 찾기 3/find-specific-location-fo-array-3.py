arr = list(map(int, input().split()))
n = len(arr)
cnt = 0
for i in range (n + 1) :
    cnt += 1
    if i == 0 :
        cnt += 1

        print(arr[cnt] + arr[cnt-1] + arr[cnt-2])