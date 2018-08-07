"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def temp_converter():
    MENU = """    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celcius = float(input("Celsius: "))
            fahrenheit = celcius_to_far(celcius)
            print("Result: {:.2f} F".format(fahrenheit))

        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celcius = far_to_celcius(fahrenheit)
            print("Result: {:.2f} C".format(celcius))

        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def celcius_to_far(celcius):
    fahrenheit = celcius * 9.0 / 5 + 32
    return fahrenheit

def far_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * (5 / 9)
    return celcius



temp_converter()




