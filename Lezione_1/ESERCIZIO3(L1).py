listanumeri=(input("inserisci 5 numeri separati da spazio"))
listanumeri=[int(numero) for numero in listanumeri.split()] 

numeripositivi =[] 

for numero in listanumeri :
    if numero >0 :
        numeripositivi.append(numero)

print(numeripositivi)

