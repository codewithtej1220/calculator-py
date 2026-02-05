def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error! Modulus by zero."
    return a % b

def power(a, b):
    return a ** b


print("Simple Calculator")
print("Operations:")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")
print("%  Modulus")
print("** Power")
print("q  Quit")

while True:
    choice = input("\nEnter choice: ")

    if choice.lower() == 'q':
        print("Exiting calculator. Goodbye!")
        break

    if choice not in ['+', '-', '*', '/', '%', '**']:
        print("Invalid operation! Please choose a valid one.")
        continue

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    if choice == '+':
        print("Result:", add(a, b))
    elif choice == '-':
        print("Result:", subtract(a, b))
    elif choice == '*':
        print("Result:", multiply(a, b))
    elif choice == '/':
        print("Result:", divide(a, b))
    elif choice == '%':
        print("Result:", modulus(a, b))
    elif choice == '**':
        print("Result:", power(a, b))
