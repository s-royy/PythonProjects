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



