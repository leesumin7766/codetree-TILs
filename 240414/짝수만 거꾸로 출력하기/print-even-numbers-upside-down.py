n = int(input())
arr = list(map(int, input().split()))
number = 0
for i in range(n , 0 , -1) :
    
    if i % 2 == 0 :
        number += i

print(number, end = " ")