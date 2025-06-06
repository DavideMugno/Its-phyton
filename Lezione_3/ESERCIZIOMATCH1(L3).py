numero=int(input("inserisci un numero"))

match numero:
    case 1:
        print("congratulazioni")
    case 2:
        print("wow gemelli")
    case 3:
        print("Wow tre")
    case 4:
        print("Mamma mia quattro")
    case 5:
        print("incredibile")
    case _:
        print(f"non ci credo {numero}bambini")