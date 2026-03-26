# Enhancement:
# - Added error handling for invalid formulas and invalid numeric input.
# - Output formatted to 5 decimal places for clarity.

from formula import parse_formula

# Index constants
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1


def make_periodic_table():
    return {
        "H": ["Hydrogen", 1.00794],
        "He": ["Helium", 4.002602],
        "Li": ["Lithium", 6.941],
        "Be": ["Beryllium", 9.012182],
        "B": ["Boron", 10.811],
        "C": ["Carbon", 12.0107],
        "N": ["Nitrogen", 14.0067],
        "O": ["Oxygen", 15.9994],
        "F": ["Fluorine", 18.9984032],
        "Ne": ["Neon", 20.1797],
        "Na": ["Sodium", 22.98976928],
        "Mg": ["Magnesium", 24.305],
        "Al": ["Aluminum", 26.9815386],
        "Si": ["Silicon", 28.0855],
        "P": ["Phosphorus", 30.973762],
        "S": ["Sulfur", 32.065],
        "Cl": ["Chlorine", 35.453],
        "K": ["Potassium", 39.0983],
        "Ca": ["Calcium", 40.078],
        "Fe": ["Iron", 55.845],
        "Cu": ["Copper", 63.546],
        "Zn": ["Zinc", 65.38],
        "Ag": ["Silver", 107.8682],
        "I": ["Iodine", 126.90447],
        "Ba": ["Barium", 137.327],
        "Au": ["Gold", 196.966569],
        "Hg": ["Mercury", 200.59],
        "Pb": ["Lead", 207.2]
    }


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    total_mass = 0

    for item in symbol_quantity_list:
        symbol = item[0]
        quantity = item[1]

        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        total_mass += atomic_mass * quantity

    return total_mass


def main():
    try:
        formula = input("Enter the molecular formula of the sample: ")
        sample_mass = float(input("Enter the mass in grams of the sample: "))

        periodic_table = make_periodic_table()

        symbol_quantity_list = parse_formula(formula)

        molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)

        number_of_moles = sample_mass / molar_mass

        print(f"{molar_mass:.5f} grams/mole")
        print(f"{number_of_moles:.5f} moles")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()