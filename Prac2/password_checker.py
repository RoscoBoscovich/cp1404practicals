"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""

    """This section determines if the length is valid"""

    if len(password) < (MIN_LENGTH) or len(password) > (MAX_LENGTH):
       print("Incorrect amount of characters, please try again")
       return False




    """here we will count the upper lower and special characters"""

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    for char in range(len(password)):
          if password[char].islower():
                count_lower = count_lower + 1
          if password[char].isupper():
                count_upper = count_upper + 1
          if password[char].isnumeric():
                count_digit = count_digit + 1
          if password[char] in SPECIAL_CHARACTERS:
                count_special = count_special + 1

    if count_lower == 0:
        return False
    if count_upper == 0:
        return False
    if count_digit == 0:
        return False
    if count_special == 0:
        return False
    pass

    return True

main()