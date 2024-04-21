arr = list(map(int, input().split()))

n = len(arr)
cnt_a = 0
cnt_b = 0

for i in range(n+1) :
    if i % 2 == 0 :
        cnt_b += i
    else :
        cnt_a += i

if cnt_a > cnt_b :
    print(cnt_a - cnt_b)
elif cnt_b > cnt_a :
    print(cnt_b - cnt_a)
else :
    print("0")