old_1 , sex_1 = input().split()
old_2 , sex_2 = input().split()

old_1 = int(old_1)
old_2 = int(old_2)


if old_1 > 18 and sex_1 == 'M' :
    print(1)
elif old_2 > 18 and sex_2 == 'M' :
    print(1)
else :
    print(0)