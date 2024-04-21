n = input()
p = input()
c = input()

len_n = len(n)
len_p = len(p)
len_c = len(c)

if len_n > len_p :
    if len_p > len_c :
        print(len_n - len_c)
    else :
        print(len_n - len_p)
elif len_p > len_n :
    if len_n > len_c :
        print(len_p - len_c)
    else :
        print(len_p - len_n)
elif len_c > len_n : 
    if len_n > len_p :
        print(len_c - len_p)
    else :
        print(len_c - len_n)