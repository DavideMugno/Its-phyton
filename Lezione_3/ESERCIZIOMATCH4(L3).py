
voto=int(input("Inserisci un voto da 66 a 110"))

match voto:
    case _ if voto >=66 and voto <= 69:
        print("1.0")
    case _ if voto >=70 and voto <= 75:
        print("1.7")
    case _ if voto >=76 and voto <= 80:
        print("2.0")
    case _ if voto >=80 and voto <= 85:
        print("2.3")
    case _ if voto >=85 and voto <= 90:
        print("2.7")
    case _ if voto >=91 and voto <= 95:
        print("3.0")
    case _ if voto >=96 and voto <=100:
        print("3.3")
    case _ if voto >=101 and voto <= 105:
        print("3.7")
    case _ if voto >=106 and voto <= 110:
        print("4.0")