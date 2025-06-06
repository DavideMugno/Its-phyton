listanumeri=input("inserisci 7 numeri separati dallo spazio ")
soglia=int(input("inserisci un numero soglia"))

listanumeri=[int (numero) for numero in listanumeri.split()]

maggioresoglia=[]

for numero in listanumeri:
    if numero > soglia:
        maggioresoglia.append(numero)

print(maggioresoglia)

