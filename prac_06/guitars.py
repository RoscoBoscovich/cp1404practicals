"""Guitar collection program"""

from prac_06.guitar_class import Guitars

def main():

    guitar_list = []

    print("My Guitars!")
    name = " "

    # while name != "":
    #     name = input("Name: ")
    #     if name == "":
    #         break
    #     year = input("Year: ")
    #     cost = input("Cost: ")
    #     guitar_list.append(Guitars(name,year,cost))
    #      print("Guitar {}: {} ({}), worth ${} added.".format(i, guitar.name, guitar.year, guitar.cost))

    guitar_list.append(Guitars("Gibson L-5 CES", 1922, 16035.40))
    guitar_list.append(Guitars("Line 6 JTV-59", 2010, 1512.9))


    print("These are my guitars")
    for i, guitar in enumerate(guitar_list):
        print("Guitar {}: {} ({}), worth ${} {}".format(i, guitar.name, guitar.year, guitar.cost, guitar.is_vintage()))

main()