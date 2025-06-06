listanumeri=input("inserisci 10 numeri separati da uno spazio")
listanumeri=[int (numero) for numero in listanumeri.split()] 

numeripari= []
numeridispari= []

for numero in listanumeri:
    if numero % 2 ==0:
        numeripari.append(numero)
    else:
        numeridispari.append(numero)

print( {len(numeripari)})
print( {len(numeridispari)})


 