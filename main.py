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
#vraag_naam_leeftijd()

def vraag_input(onderwerp):
    onderwerp = input("Geef me een onderwerp")
    return onderwerp
def print_verhaal(naam,dier,plaats):
    print("er was eens een man met de naam",naam,"zijn lievelings dier was",dier,"en hij woonde in",plaats,)
def verhaal_generator():
    print("Welkom bij de verhaalgenerator")
    naam = vraag_input("naam")
    dier = vraag_input("dier")
    plaats = vraag_input("plaats")
    print(print_verhaal(naam,dier,plaats))
    print("Het einde van het verhaal")
verhaal_generator()
