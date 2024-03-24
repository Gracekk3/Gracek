
zacatek = int(input("Zadejte začátek intervalu: "))
konec = int(input("Zadejte konec intervalu: "))

for cislo in range(zacatek, konec + 1):
    print(cislo, end=", " if cislo != konec else "")
