arr = list(map(int, input().split()))
n = len(arr)
for i in range (n + 1) :
    if i == 0 :
        print(i + arr[i -1] + arr[i-2])