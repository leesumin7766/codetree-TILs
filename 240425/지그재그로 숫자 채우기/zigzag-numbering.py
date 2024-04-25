n , m = tuple(map(int, input().split()))


arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]
count = 0

for col in range(m) :
    if col % 2 == 0 :
        for row in range(n) :
            arr[row][col] = count
            count += 1
    else :
        for row in range(n - 1, -1, -1) :
            arr[row][col] = count
            count += 1

for row in range(n) :
    for col in range(m) :
        print(arr[row][col], end = " ")
    print()