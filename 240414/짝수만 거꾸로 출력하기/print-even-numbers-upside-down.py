n = int(input())
arr = list(map(int, input().split()))

i = 0
for arr in range(n , 0 , -1) :
    
    if arr % 2 == 0 :
        i += arr
        
print(i, end = " ")