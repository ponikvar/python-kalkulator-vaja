def sestej(a, b):
    return a + b
def odstej(a, b):
    return a - b
def pomnozi(a, b):
    return a * b
def deli(a, b):
    if b == 0:
        print("Napaka: deljenje z 0 ni dovoljeno!")
        return None
    return a / b
zgodovina = []
def dodaj_zgodovino(izraz):
    zgodovina.append(izraz)
    if len(zgodovina) > 3:
        zgodovina.pop(0)
print("Pozdrav! Mini kalkulator")
print("0 = izhod")
print("1 = seštevanje")
print("2 = odštevanje")
print("3 = množenje")
print("4 = deljenje")
print("5 = prikaži zgodovino zadnjih 3 izračunov")

while True:
    izbira = input("Kaj želiš narediti? (0-5): ")

    if izbira == "0":
        print("Izhod iz programa. Nasvidenje!")
        break
    elif izbira == "1":
        x = float(input("Prvo število: "))
        y = float(input("Drugo število: "))
        rezultat = sestej(x, y)
        print(f"{x} + {y} = {rezultat}")
        dodaj_zgodovino(f"{x} + {y} = {rezultat}")
    elif izbira == "2":
        x = float(input("Prvo število: "))
        y = float(input("Drugo število: "))
        rezultat = odstej(x, y)
        print(f"{x} - {y} = {rezultat}")
        dodaj_zgodovino(f"{x} - {y} = {rezultat}")
    elif izbira == "3":
        x = float(input("Prvo število: "))
        y = float(input("Drugo število: "))
        rezultat = pomnozi(x, y)
        print(f"{x} * {y} = {rezultat}")
        dodaj_zgodovino(f"{x} * {y} = {rezultat}")
    elif izbira == "4":
        x = float(input("Prvo število: "))
        y = float(input("Drugo število: "))
        rezultat = deli(x, y)
        if rezultat is not None:
            print(f"{x} / {y} = {rezultat}")
            dodaj_zgodovino(f"{x} / {y} = {rezultat}")
    elif izbira == "5":
        print("Zgodovina zadnjih 3 izračunov:")
        for z in zgodovina:
            print(z)
    else:
        print("Neveljavna izbira!")
