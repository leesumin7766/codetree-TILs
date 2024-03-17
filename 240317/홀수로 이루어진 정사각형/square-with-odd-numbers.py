n = int(input())

for i in range (n) :
    for j in range(1, n + n, 2) :
        print(10 + j + (i * 2) , end = " ")
    print()