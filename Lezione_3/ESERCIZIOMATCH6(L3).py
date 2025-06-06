animale=input("inserisci un animale")


Mammiferi=["cane","gatto","cavallo","elefante","leone"] 
Rettili=["serpente","lucertola","tartaruga","coccodrillo"] 
Uccelli=["aquila", "pappagallo", "gufo", "falco"] 
Pesci= ["squalo", "trota", "salmone", "carpa"] 

match animale:
    case mammiferi:
        print("L'animale è un mammifero")