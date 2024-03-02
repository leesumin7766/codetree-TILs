ma , ea = input().split()
mb , eb = input().split()

ma = int(ma)
mb = int(mb)
ea = int(ea)
eb = int(eb)
if ma > mb :
    print("A")
elif ma == mb and ea > eb :
    print("A")
else :
    print("B")