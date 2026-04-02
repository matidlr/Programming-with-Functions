""""
Enhancement: Added a 'Return By' date exactly 30 days in the future (at 9:00 PM).
"""

import csv
from datetime import datetime, timedelta

def main():
    
    PRODUCT_ID_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2

    
    REQ_ID_INDEX = 0
    REQ_QUANTITY_INDEX = 1

    
    SALES_TAX_RATE = 0.06

    try:
        
        products_dict = read_dictionary("products.csv", PRODUCT_ID_INDEX)

        print("Inkom Emporium")
        print()

        
        total_items = 0
        subtotal = 0.0

        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)  # Skip the header row

           
            for row in reader:
                product_id = row[REQ_ID_INDEX]
                quantity = int(row[REQ_QUANTITY_INDEX])

                
                product_info = products_dict[product_id]
                
                name = product_info[NAME_INDEX]
                price = float(product_info[PRICE_INDEX])

                
                print(f"{name}: {quantity} @ {price}")

                
                total_items += quantity
                subtotal += (quantity * price)

        
        sales_tax = subtotal * SALES_TAX_RATE
        total_due = subtotal + sales_tax

        print()
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total_due:.2f}")

        print()
        print("Thank you for shopping at the Inkom Emporium.")

        
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")

        # Enhancement: Return Date (30 days from now at 9:00 PM)
        return_date = current_date_and_time + timedelta(days=30)
        print(f"Return by: {return_date:%b %d, %Y} 9:00 PM")

    except FileNotFoundError as file_err:
        print("Error: missing file")
        print(file_err)

    except PermissionError as perm_err:
        print("Error: you do not have permission to access this file.")
        print(perm_err)

    except KeyError as key_err:
        print("Error: unknown product ID in the request.csv file")
        print(key_err)

def read_dictionary(filename, key_column_index):
    """
    Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    """
    dictionary = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header

        for row_list in reader:
            if len(row_list) > 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list

    return dictionary

if __name__ == "__main__":
    main()