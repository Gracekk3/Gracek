import random


numbers = [random.randint(1, 100) for _ in range(10)]


print("Původní pole:", numbers)


sorted_numbers = sorted(numbers)


print("Seřazené pole:", sorted_numbers)
