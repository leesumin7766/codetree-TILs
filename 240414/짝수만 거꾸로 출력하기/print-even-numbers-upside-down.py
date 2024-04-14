n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n , 0 , -1) :
    
    if i % 2 == 0 :
        cnt += i

print(cnt, end = " ")