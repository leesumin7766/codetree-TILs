sex = int(input())
old = int(input())


if sex == 0 :
    if old > 18 :
        print("MAN")
    else :
        print("BOY")

if sex == 1 :
    if old > 18 :
        print("WOMAN")
    else :
        print("GIRL")