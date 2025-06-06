oggetti = []
for i in range(3):
    oggetto = input("Inserisci un oggetto: ")
    oggetti.append(oggetto)

oggetti.sort()  

match oggetti:
    case ["latte", "pane", "uova"]:
        print("materiale alimentare")
    case ["matita", "penna", "quaderno"]:
        print("materiale scolastico")
    case ["armadio", "sedia", "tavolo"]:
        print("materiale edile")
    case ["computer", "tablet", "telefono"]:
        print("materiale informatico")
    case _:
        print("lista sconosciuta")

