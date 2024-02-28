cm , kg = input().split()
cm = float(cm)
kg = float(kg)
bmi = ((kg * 10000)/ (cm * cm))
bmi = int(bmi)
if bmi < 25:
    print(bmi)
else :
    print(bmi)
    print("Obesity")