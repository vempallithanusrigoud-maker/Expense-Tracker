import json
import os
from datetime import date

FILE_NAME = "expenses.json"


def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {"income": 0.0, "expenses": []}


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_income(data):
    try:
        amount = float(input("Enter income amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        data["income"] += amount
        save_data(data)
        print("Income added successfully!")
    except ValueError:
        print("Please enter a valid amount.")


def add_expense(data):
    try:
        title = input("Enter expense name: ").strip()
        if not title:
            print("Expense name cannot be empty.")
            return

        category = input("Enter category (Food/Travel/Study/Other): ").strip()
        if not category:
            print("Category cannot be empty.")
            return

        amount = float(input("Enter expense amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        data["expenses"].append({
            "title": title,
            "category": category,
            "amount": amount,
            "date": str(date.today())
        })
        save_data(data)
        print("Expense added successfully!")
    except ValueError:
        print("Please enter a valid amount.")


def view_expenses(data):
    if not data["expenses"]:
        print("No expenses recorded yet.")
        return

    print("\n--- Expense Records ---")
    for number, expense in enumerate(data["expenses"], start=1):
        print(
            f"{number}. {expense['title']} | "
            f"{expense['category']} | "
            f"Rs. {expense['amount']:.2f} | "
            f"{expense['date']}"
        )


def show_summary(data):
    total = sum(item["amount"] for item in data["expenses"])
    balance = data["income"] - total

    print("\n--- Financial Summary ---")
    print(f"Total Income:   Rs. {data['income']:.2f}")
    print(f"Total Expenses: Rs. {total:.2f}")
    print(f"Balance:        Rs. {balance:.2f}")


def main():
    data = load_data()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. Show Summary")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_income(data)
        elif choice == "2":
            add_expense(data)
        elif choice == "3":
            view_expenses(data)
        elif choice == "4":
            show_summary(data)
        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")


if __name__ == "__main__":
    main()