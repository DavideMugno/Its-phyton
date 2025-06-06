numeri=range(1,21)
pari=[]
dispari=[]

for i in numeri:
    if i %2==0:
        pari.append(i)
    else:
        dispari.append(i)

print(dispari)