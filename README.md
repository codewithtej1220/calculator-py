def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Error! Division by zero."

def modulus(x, y):
    return x % y if y != 0 else "Error! Division by zero."

def power(x, y):
    return x ** y

while True:
    print("\nSimple Calculator")
    print("Choose operation: +, -, *, /, %, ** (exponent) or q to quit")

    choice = input("Enter choice: ")

    if choice.lower() == 'q':
        print("Exiting calculator. Goodbye!")
        break

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
    else:
        print("Invalid operation! Please choose a valid one.")
