"""
Enhancement Explanation:
This program exceeds the assignment requirements by adding a "Return By" date.
At the bottom of the receipt, the program calculates a return deadline that is
30 days in the future at 9:00 PM and displays it to the user.

This feature demonstrates additional use of Python's datetime module and adds
real-world functionality similar to actual store receipts.
"""

import csv
from datetime import datetime, timedelta

TAX_RATE = 0.06


def read_dictionary(filename, key_column_index):
    """Reads CSV file into a dictionary."""
    products_dict = {}

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        for row in reader:
            key = row[key_column_index]
            products_dict[key] = row

    return products_dict


def main():
    try:
        print("Inkom Emporium")

        products_dict = read_dictionary("products.csv", 0)

        total_items = 0
        subtotal = 0

        print()

        with open("request.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header

            for row in reader:
                product_id = row[0]
                quantity = int(row[1])

                product = products_dict[product_id]
                name = product[1]
                price = float(product[2])

                print(f"{name}: {quantity} @ {price:.2f}")

                total_items += quantity
                subtotal += price * quantity

        print()
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")

        sales_tax = subtotal * TAX_RATE
        print(f"Sales Tax: {sales_tax:.2f}")

        total = subtotal + sales_tax
        print(f"Total: {total:.2f}")

        print("\nThank you for shopping at the Inkom Emporium.")

        # Current date and time
        now = datetime.now()
        print(now.strftime("%a %b %d %H:%M:%S %Y"))

        #EXCEEDING REQUIREMENT: Return-by date (30 days later at 9 PM)
        return_date = now + timedelta(days=30)
        return_date = return_date.replace(hour=21, minute=0, second=0)
        print("Return by:", return_date.strftime("%a %b %d %H:%M:%S %Y"))

    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)

    except PermissionError as e:
        print("Error: permission denied")
        print(e)

    except KeyError as e:
        print("Error: unknown product ID in the request.csv file")
        print(e)


if __name__ == "__main__":
    main()