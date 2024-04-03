arr = list(map(int, input().split()))
cnt = 0
sum_val = 0
for elem in arr :
    if elem == 0 :
        break
    else :
        sum_val += elem
        cnt += 1

avg = sum_val / cnt
print(sum_val , avg)