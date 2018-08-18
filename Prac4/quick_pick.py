"""  QUICK PICK LOTTERY TICKET NUMBER GENERATOR"""

from random import shuffle

# Generate list of 45 numbers and shuffle them
number_of_picks = int(input("How many quick picks would you like to generate?"))
list_of_numbers = list(range(45))
list_of_numbers = [number+1 for number in list_of_numbers]
shuffle(list_of_numbers)
shuffle(list_of_numbers)
shuffle(list_of_numbers)


# Take the first five numbers from the list and reshuffle
for quick_pick_number in range(number_of_picks):
    quick_pick = []
    quick_pick = [list_of_numbers[x] for x in range(5)]
    shuffle(list_of_numbers)
    print(sorted(quick_pick))

