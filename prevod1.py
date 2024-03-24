
hodiny = int(input("Zadejte počet hodin: "))

dny = hodiny // 24
zbyvajici_hodiny = hodiny % 24

print("Časový údaj v dnech a hodinách:", dny, "dnů,", zbyvajici_hodiny, "hodin")
