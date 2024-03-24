import random


numbers = [random.randint(1, 100) for _ in range(10)]

# Výpis prvků pole
for number in numbers:
    print(number)
