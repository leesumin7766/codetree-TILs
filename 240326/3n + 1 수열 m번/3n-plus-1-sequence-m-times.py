m = int(input())

for i in range (m) :
    n = int(input())
    sum = 0
    
    while n != 1 :
        if n % 2 == 0 :
            n = n / 2
            sum += 1
            continue 
    
        elif n % 2 == 1 :
            n = n * 3 + 1
            sum += 1
            continue 
    
    print(sum)