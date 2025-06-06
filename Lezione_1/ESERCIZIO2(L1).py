listanumeri=(input("inserisci 4 numeri separati da uno spazio"))
listanumeri=[int(numero) for numero in listanumeri.split()] 
print (f"il numero piu grande dei 4 numeri è = {max(listanumeri)}")