nome=input("inserisci il tuo nome")
genere=input("inserisci m per maschio o f per femmina")

match genere:
    case "m":
        print(f"nome:{nome} \n genere:Maschio")
    case "f":
        print(f"nome:{nome} \n genere:Femmina")
    