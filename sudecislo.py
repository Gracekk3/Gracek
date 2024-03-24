def je_sude(number):
    return number % 2 == 0


input_number = int(input("Zadejte číslo: "))

8
if je_sude(input_number):
    print(f"Číslo {input_number} je sudé.")
else:
    print(f"Číslo {input_number} není sudé.")
