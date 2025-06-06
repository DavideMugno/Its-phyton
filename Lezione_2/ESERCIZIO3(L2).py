numeri=input("inserisci tre numeri separati da uno spazio")
numeri=[int(numero)for numero in numeri.split()]

qntnumeri=len(numeri)
somma=sum(numeri)

media=somma/qntnumeri

print(media)
print(somma)
print(qntnumeri)
    