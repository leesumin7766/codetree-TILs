arr = list(map(int , input().split()))

n = len(arr)
sum_val = 0
sum_val2 = 0
cnt = 0

for i in range(10) :
    if (i + 1) % 2 == 0 :
        sum_val += arr[i]
    
    if (i + 1) % 3 == 0 :
        sum_val2 += arr[i]
        cnt += 1
avg = sum_val2 / cnt 
print(sum_val , round(avg, 1))