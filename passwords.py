"""
Enhancement:
- After checking the password strength, the program also prints the numeric
  strength score (0–5) so users learn what rating their password received.
"""

LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
         "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
         "y", "z"]

UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
         "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
         "Y", "Z"]

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_",
           "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",",
           ".", "<", ">", "?", "/", "\\", "`", "~"]


# ------------------------------------------------
# Function: word_in_file
# ------------------------------------------------
def word_in_file(word, filename, case_sensitive=False):
    """
    Reads a file where each line contains one word.
    Returns True if word is found, otherwise False.

    If case_sensitive is False, match is case-insensitive.
    """

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            file_word = line.strip()

            if case_sensitive:
                if word == file_word:
                    return True
            else:
                if word.lower() == file_word.lower():
                    return True

    return False


# ------------------------------------------------
# Function: word_has_character
# ------------------------------------------------
def word_has_character(word, character_list):
    """
    Returns True if any character in word is found in character_list.
    """

    for char in word:
        if char in character_list:
            return True

    return False


# ------------------------------------------------
# Function: word_complexity
# ------------------------------------------------
def word_complexity(word):
    """
    Calculates complexity score based on 4 character types:
    LOWER, UPPER, DIGITS, SPECIAL

    Returns an integer from 0 to 4.
    """

    complexity = 0

    if word_has_character(word, LOWER):
        complexity += 1

    if word_has_character(word, UPPER):
        complexity += 1

    if word_has_character(word, DIGITS):
        complexity += 1

    if word_has_character(word, SPECIAL):
        complexity += 1

    return complexity


# ------------------------------------------------
# Function: password_strength
# ------------------------------------------------
def password_strength(password, min_length=10, strong_length=16):
    """
    Determines password strength (0–5) based on requirements.

    Prints required security messages and returns strength score.
    """

    # Check dictionary word (case insensitive)
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    # Check known top passwords (case sensitive)
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # Too short check
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    # Long password check
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    # Complexity-based strength score
    complexity = word_complexity(password)

    strength = 1 + complexity

    return strength


# ------------------------------------------------
# Function: main
# ------------------------------------------------
def main():
    """
    User loop for checking password strength.
    User quits by entering q or Q.
    """

    print("Password Strength Checker")
    print("Enter Q to quit.\n")

    while True:
        password = input("Enter a password to test: ")

        if password.lower() == "q":
            print("Goodbye!")
            break

        strength = password_strength(password)

        # Enhancement: show numeric score
        print(f"Password strength score: {strength}/5\n")


# Required testing entry point
if __name__ == "__main__":
    main()
