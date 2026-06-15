from .expense import Expense
from .expense_manager import ExpenseManager
from .file_handler import load_data, save_data, export_csv
from .reports import monthly_report, category_report, stats


FILE = "data/expenses.json"


class FinanceTracker:
    def __init__(self):
        self.manager = ExpenseManager()
        self.data = load_data(FILE)

        self.budget = self.data.get("budget", 0)

        for e in self.data["expenses"]:
            self.manager.add(e)

    def run(self):
        print("=" * 60)
        print("          PERSONAL FINANCE TRACKER")
        print("=" * 60)

        while True:
            print("\n" + "=" * 40)
            print("              MAIN MENU")
            print("=" * 40)
            print("1. Add New Expense")
            print("2. View All Expenses")
            print("3. Search Expenses")
            print("4. Generate Monthly Report")
            print("5. View Category Breakdown")
            print("6. Set/Update Budget")
            print("7. Export Data to CSV")
            print("8. View Statistics")
            print("9. Backup/Restore Data")
            print("0. Exit")
            print("=" * 40)

            choice = input("\nEnter your choice (0-9): ").strip()

            if choice == "1":
                self.add_expense()

            elif choice == "2":
                self.view_expenses()

            elif choice == "3":
                self.search_expenses()

            elif choice == "4":
                self.generate_report()

            elif choice == "5":
                self.category_breakdown()

            elif choice == "6":
                self.set_budget()

            elif choice == "7":
                self.export_data()

            elif choice == "8":
                self.view_stats()

            elif choice == "9":
                self.backup()

            elif choice == "0":
                self.exit_app()
                break

            else:
                print("Invalid choice! Please enter 0-9.")

    # ---------------- FEATURES ----------------

    def add_expense(self):
        print("\n--- ADD NEW EXPENSE ---")

        try:
            date = input("Date (YYYY-MM-DD): ")
            amount = float(input("Amount: "))
            category = input("Category: ")
            description = input("Description: ")

            if not Expense.validate(date, amount, category):
                print("Invalid expense data!")
                return

            expense = {
                "date": date,
                "amount": amount,
                "category": category,
                "description": description
            }

            self.manager.add(expense)
            save_data(FILE, {
                "expenses": self.manager.all(),
                "budget": self.budget
            })

            print("Expense added successfully!")

        except ValueError:
            print("Invalid input!")

    def view_expenses(self):
        print("\n--- ALL EXPENSES ---")

        if not self.manager.all():
            print("No expenses found.")
            return

        for i, e in enumerate(self.manager.all(), 1):
            print(f"{i}. {e['date']} | ₹{e['amount']} | {e['category']} | {e['description']}")

    def search_expenses(self):
        print("\n--- SEARCH EXPENSES ---")
        key = input("Enter keyword: ")
        results = self.manager.search(key)

        if not results:
            print("No matching expenses.")
            return

        for r in results:
            print(r)

    def generate_report(self):
        print("\n--- MONTHLY REPORT ---")
        month = input("Enter month (YYYY-MM): ")
        total = monthly_report(self.manager.all(), month)
        print(f"Total expenses for {month}: ₹{total}")

    def category_breakdown(self):
        print("\n--- CATEGORY BREAKDOWN ---")
        result = category_report(self.manager.all())

        for k, v in result.items():
            print(f"{k}: ₹{v}")

    def set_budget(self):
        print("\n--- SET/UPDATE BUDGET ---")
        self.budget = float(input("Enter budget: "))
        print("Budget updated!")

    def export_data(self):
        print("\n--- EXPORT DATA ---")
        export_csv("data/exports/export.csv", self.manager.all())
        print("Exported successfully!")

    def view_stats(self):
        print("\n--- STATISTICS ---")
        s = stats(self.manager.all())
        print(f"Total: ₹{s['total']}")
        print(f"Average: ₹{s['avg']}")
        print(f"Max: ₹{s['max']}")

    def backup(self):
        print("\n--- BACKUP ---")
        save_data("data/backup/backup.json", {
            "expenses": self.manager.all(),
            "budget": self.budget
        })
        print("Backup created!")

    def exit_app(self):
        save_data(FILE, {
            "expenses": self.manager.all(),
            "budget": self.budget
        })

        print("\n" + "=" * 60)
        print("Thank you for using Personal Finance Tracker!")
        print("=" * 60)


def main():
    app = FinanceTracker()
    app.run()


if __name__ == "__main__":
    main()