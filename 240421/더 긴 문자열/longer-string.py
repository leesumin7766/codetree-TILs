n , p  = input().split()

len_n = len(n)
len_p = len(p)

if len_n > len_p :
    print(n,len_n)
elif len_n < len_p :
    print(p ,len_p)
else :
    print("same")