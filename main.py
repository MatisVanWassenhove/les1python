def vriend(naam):
    print("Hallo",naam,"leuk je te zien")
vriend("Bob")

def papegaai(getal):
    return getal * 3
print(papegaai("hoi"))

def vraag_naam_leeftijd():
    naam = input("Wat is je naam?")
    leeftijd = int(input("Wat is je leeftijd"))
    print("Je naam is", naam, "en je leeftijd is ", leeftijd)
vraag_naam_leeftijd()
