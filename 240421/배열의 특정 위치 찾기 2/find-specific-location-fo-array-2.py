arr = list(map(int, input().split()))

sum_a = 0
sum_b = 0

for i in range(10) :
    if i % 2 == 0 :
        sum_b += arr[i]
    else :
        sum_a += arr[i]

if sum_a > sum_b :
    print(sum_a - sum_b)
elif sum_b > sum_a :
    print(sum_b - sum_a)
else :
    print("0")