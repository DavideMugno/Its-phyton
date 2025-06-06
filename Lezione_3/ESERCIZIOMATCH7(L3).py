nomepersona=input("inserisci un nome")
etapersona=int(input("inserisci un età"))
ruolopersona=input("inserisci un ruolo")



persona={

    "nome":nomepersona,
    "eta":etapersona,
    "ruolo":ruolopersona
}              

match persona:
    case _ if persona["ruolo"] =="admin":
        print("accesso a tutte le funzioni")
    case _ if persona["ruolo"] =="moderatore":
        print("Può gestire i contenuti ma non modificare le impostazioni")
    case _ if persona["eta"] >=18:
        print("Accesso standard a tutti i servizi")
    case _ if persona["eta"]<=18:
        print("Accesso limitato!Alcune funzionalità sono bloccate")
    case _ if persona["ruolo"]=="ospite":
        print("accesso ristretto")   
