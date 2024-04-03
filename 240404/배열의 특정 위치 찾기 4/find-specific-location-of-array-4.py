arr = list(map(int, input().split()))

cnt = 0
sum_val = 0
for elem in arr :
    if elem % 2 == 0 and elem != 0:
        sum_val += elem
        cnt += 1 
    if elem == 0 :
        break 

print(cnt , sum_val)