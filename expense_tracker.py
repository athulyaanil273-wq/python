expenses = []

print("Simple Expense Tracker")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append((name, amount))
        print("Expense added successfully.")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nYour Expenses:")
            for name, amount in expenses:
                print(name, "-", amount)

    elif choice == "3":
        total = sum(amount for name, amount in expenses)
        print("Total Expense:", total)

    elif choice == "4":
        print("Thank you for using the Expense Tracker.")
        break

    else:
        print("Invalid choice. Please try again.")
