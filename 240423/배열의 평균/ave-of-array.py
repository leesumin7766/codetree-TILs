arr_2d = [
    list(map(int, input().split()))
    for _ in range(2)
]
for i in range(2) :
    sum_val1 = 0
    for j in range(4) :
        sum_val1 += arr_2d[i][j]
    print(f"{sum_val1 / 4 :.1f}", end = " ")
print()

for j in range(4) :
    sum_val2 = 0
    for i in range(2) :
        sum_val2 += arr_2d[i][j]
    print(f"{sum_val2 / 2 :.1f}", end = " ")
print()

sum_val = 0
for i in range(4) :
    for j in range(2) :
        sum_val += arr_2d[j][i]
print(f"{sum_val / 8 :.1f}")