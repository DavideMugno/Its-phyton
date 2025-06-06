invitati=["Travis","Martina","Aqui"]

invitati.append("Diego")
invitati.remove("Travis")
invitati.insert(len(invitati),"Leo")
invitati.insert(len(invitati),"Davide")
invitati.insert(len(invitati),"Cillo")


for i in invitati:
    print(f"Vorresti venire a casa mia {i}?")

print("purtroppo Travis non può piu venire")
