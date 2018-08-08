

def ascii_converter():
    MENU = """    A - Convert ASCII to character
    C - Convert Character to ASCII
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "A":
            ascii_input = (input("Enter a character: "))

            print("The ASCII code for {} is {}".format()

        elif choice == "C":
            char_input = (input("Enter a number between 33 and 127: "))


        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


Enter a character: g
The ASCII code for g is 103
Enter a number between 33 and 127: 100
The character for 100 is d