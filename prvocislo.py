def je_prvocislo(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Zadejte číslo: "))
if je_prvocislo(number):
    print(f"{number} je prvočíslo.")
else:
    print(f"{number} není prvočíslo.")
5