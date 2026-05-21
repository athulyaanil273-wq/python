# Simple Calculator

while True:
    print("\n===== Simple Calculator =====")
    print("1. Addition       (+)")
    print("2. Subtraction    (-)")
    print("3. Multiplication (*)")
    print("4. Division       (/)")
    print("5. Modulus        (%)")
    print("0. Exit")

    choice = input("\nEnter choice: ")

    if choice == "0":
        print("Goodbye!")
        break

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice! Try again.")
        continue

    a = float(input("Enter first number : "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print(f"Result: {a} + {b} = {a + b}")
    elif choice == "2":
        print(f"Result: {a} - {b} = {a - b}")
    elif choice == "3":
        print(f"Result: {a} * {b} = {a * b}")
    elif choice == "4":
        if b == 0:
            print("Error! Cannot divide by zero.")
        else:
            print(f"Result: {a} / {b} = {a / b}")
    elif choice == "5":
        print(f"Result: {a} % {b} = {a % b}")
