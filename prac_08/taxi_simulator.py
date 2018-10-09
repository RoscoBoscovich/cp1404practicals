

from prac_08.taxi import Taxi
from prac_08.silverservicetaxi import SilverServiceTaxi


def taxi_simulator():

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_to_date = 0

    print("Let's Drive")
    display_menu()
    menu_choice = input()

    while menu_choice != 'q':

        if menu_choice == 'c':
            current_taxi = choose_taxi(taxis)

        if menu_choice == 'd':
            bill_to_date =  drive_taxi(current_taxi, bill_to_date)

        print("Bill to date ${}".format(bill_to_date))
        display_menu()
        menu_choice = input()


def display_menu():
    print("q)uit, c)hoose taxi, d)rive")


def choose_taxi(taxis):
    print("Taxis available:")
    for taxi in enumerate(taxis):
        print("{} - {}".format(taxi[0], taxi[1]))
    chosen_taxi = input("Choose taxi: ")
    current_taxi = taxis[int(chosen_taxi)]
    #print(current_taxi)
    return current_taxi


def drive_taxi(current_taxi, bill_to_date):
    #print(current_taxi)
    distance = int(input("Drive how far? "))
    current_taxi.drive(distance)
    bill_to_date = bill_to_date + current_taxi.get_fare()
    print(bill_to_date)
    print("Your {} trip cost you ${}".format(current_taxi.name, current_taxi.get_fare()))
    return bill_to_date

taxi_simulator()