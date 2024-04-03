arr = list(map(int, input().split()))

cnt = 0

for elem in arr :
    
    if elem == 0 :
        cnt += 1
        break 
    else :
        cnt += 1
    
for i in range(cnt -2 , -1 , -1) :
    print(arr[i], end = " ")