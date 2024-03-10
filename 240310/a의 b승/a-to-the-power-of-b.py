a , b = input().split()

a = int(a)
b = int(b)

prod = 1

for i in range(b) :
    prod *= a
print(prod)