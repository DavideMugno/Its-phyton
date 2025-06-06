opzione = ""
contatore = 20

while opzione != "exit":
    opzione = input("Inserisci un'opzione tra prenota, libera, visualizza, exit per uscire: ")

    if contatore == 0:
        print("Non ci sono più posti disponibili.")
        
    elif contatore > 0:
        if opzione == "prenota":
            print("Hai prenotato un posto.")
            contatore -= 1

        elif opzione == "libera":
            print("Hai liberato un posto.")
            contatore += 1

        elif opzione == "visualizza":
            print(f"Il numero dei posti disponibili è: {contatore}")
        
        else:
            print("Opzione non valida. Per favore, scegli una delle opzioni valide: prenota, libera, visualizza o exit.")




    


        
