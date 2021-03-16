def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select from below:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n\n")

while True:
    choice = input("Pick [1/2/3/4]: ")
    if choice in ("1", "2", "3", "4"):
        num1 = float(input("1st Number: "))
        num2 = float(input("2nd Number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid input.")