reddito=int(input("inserisci reddito familiare"))
mediavoti=int(input("inserisci la media voti"))

if reddito < 20000 and mediavoti>27:
    print("hai la borsa di studio")
else:
    print("reddito superiore o media voto insufficiente")