def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Take input from the user
num1 = float(input("Enter první číslo: "))
num2 = float(input("Enter druhé číslo: "))
choice = input("Enter operace (+, -, *, /): ")

if choice == '+':
    print(add(num1, num2))
elif choice == '-':
    print(subtract(num1, num2))
elif choice == '*':
    print(multiply(num1, num2))
elif choice == '/':
    print(divide(num1, num2))
else:
    print("nefunguje")