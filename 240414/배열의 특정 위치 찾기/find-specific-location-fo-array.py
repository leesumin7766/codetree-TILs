arr = list(map(int , input().split()))

n = len(arr)
sum_val = 0
sum_val2 = 0
cnt = 0

for i in range(n + 1) :
    if i % 2 == 0 :
        sum_val += i
    
    if i % 3 == 0 :
        sum_val2 += i
        cnt += 1
avg = sum_val2 / cnt
print(sum_val , avg)