n = int(input())


for i in range(n) :
    inp = input()
    arr = inp.split()
    a , b = int(arr[0]) , int(arr[1])
    cnt = 1
    for j in range(a , b + 1) :
        
        cnt *= j
        

    print(cnt)