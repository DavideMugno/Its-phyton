listavenditori=[]
listavendite=[]

for i in range(5):
    venditore=input("inserisci il nome di un vendiore")
    vendite=int(input("inserisci il totale delle vendite"))

    listavenditori.append(venditore)
    listavendite.append(vendite)

maxvendite=max(listavendite)
minvendite=min(listavendite)

indicemassimo=listavendite.index(maxvendite)
indiceminimo=listavendite.index(minvendite)

print(f"il vendite con piu vendite è:{listavenditori[indicemassimo]}con vendite{maxvendite}")
print(f"il vendite con piu vendite è:{listavenditori[indiceminimo]}con vendite{minvendite}")




