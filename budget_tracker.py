import csv


def read_expenses(filename):
    expenses = []

    try:
        with open(filename, newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                try:
                    expense = {
                        "date": row[0],
                        "description": row[1],
                        "category": row[2],
                        "amount": float(row[3])
                    }
                    expenses.append(expense)

                except (IndexError, ValueError):
                    print("Skipping invalid row:", row)

    except FileNotFoundError:
        print("File not found.")

    return expenses


def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def calculate_category_totals(expenses):
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    return category_totals


def calculate_average(expenses):
    if len(expenses) == 0:
        return 0

    total = calculate_total(expenses)
    return total / len(expenses)


def display_report(total, category_totals, average, count):
    print("\n--- Budget Report ---")
    print(f"Total Spending: ${total:.2f}")
    print(f"Number of Transactions: {count}")
    print(f"Average Spending: ${average:.2f}\n")

    print("Spending by Category:")
    for category, amount in category_totals.items():
        print(f"{category}: ${amount:.2f}")


def main():
    filename = "expenses.csv"

    expenses = read_expenses(filename)

    if not expenses:
        print("No valid expenses to display.")
        return

    total = calculate_total(expenses)
    category_totals = calculate_category_totals(expenses)
    average = calculate_average(expenses)

    display_report(total, category_totals, average, len(expenses))


if __name__ == "__main__":
    main()