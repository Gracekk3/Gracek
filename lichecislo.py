def je_liche(number):
    return number % 2 != 0


input_number = int(input("Zadejte číslo: "))


if je_liche(input_number):
    print(f"Číslo {input_number} je liché.")
else:
    print(f"Číslo {input_number} není liché.")
