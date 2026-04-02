import csv

def main():
    # The column headings and indexes.
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1

    # Read the contents of a CSV file named students.csv
    # into a dictionary named students_dict.
    # The I-Number is used as the key.
    students_dict = read_dictionary("students.csv", I_NUMBER_INDEX)

    # Get an I-Number from the user.
    inumber = input("Please enter an I-Number (xx-xxx-xxxx): ")

    # The I-Numbers are stored in the CSV file as digits only,
    # so we remove all dashes from the user's input.
    inumber = inumber.replace("-", "")

    # Validation logic for the user's input
    if not inumber.isdigit():
        print("Invalid character in I-Number")
    else:
        if len(inumber) < 9:
            print("Invalid I-Number: too few digits")
        elif len(inumber) > 9:
            print("Invalid I-Number: too many digits")
        else:
            # The input is valid. Now check if it exists in our dictionary.
            if inumber not in students_dict:
                print("No such student")
            else:
                # Retrieve the student list (value) from the dictionary
                # and extract the name using the NAME_INDEX.
                student_data = students_dict[inumber]
                name = student_data[NAME_INDEX]

                # Print the result.
                print(name)


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: 
        A compound dictionary containing the CSV data.
    """
    # Initialize an empty dictionary
    dictionary = {}

    # Open the file using a 'with' block for safe handling
    with open(filename, "rt") as csv_file:
        # Create the csv reader object
        reader = csv.reader(csv_file)

        # Skip the header row
        next(reader)

        # Iterate through each row in the file
        for row_list in reader:
            # If the row is not empty, process it
            if len(row_list) > 0:
                # Extract the key based on the provided index
                key = row_list[key_column_index]
                
                # Store the entire row list as the value
                dictionary[key] = row_list

    return dictionary


# Standard boilerplate to ensure main() only runs if executed directly
if __name__ == "__main__":
    main()