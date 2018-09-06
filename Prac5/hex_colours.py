"""
program to look up colour hex values
"""


def main():
    hex_colour_dict = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1" : "	#7fffd4", "azure1": "#f0ffff",
                   "beige": "#f5f5dc", "black": "#000000", "blue1": "#0000ff", "brown": "#a52a2a"}

    colour_to_find = input("Colour name:")
    while colour_to_find != "":
        if colour_to_find in  hex_colour_dict:
            print(hex_colour_dict[colour_to_find])
        else:
            print("Colour not found")
        colour_to_find = input("Colour name:")


main()

