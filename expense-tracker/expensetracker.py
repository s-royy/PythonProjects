import json
import os


FILE = "expenses.json"


def load_expenses():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)


def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=2)


def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    expenses.append({
        "amount": amount,
        "category": category,
        "description": description
    })

    save_expenses(expenses)
    print("Expense added.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    total = 0
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['amount']} | {exp['category']} | {exp['description']}")
        total += exp["amount"]

    print(f"\nTotal: {total}")


def main():
    expenses = load_expenses()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter choice (1-3): ").strip()

        if choice == "3":
            print("Goodbye!")
            break

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
