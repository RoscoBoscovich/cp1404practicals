
"""
loops program



for i in range(0,101,10):
    print(i)


J = 20
for i in range(20):
    print(J)
    J = J -1


star_number = int(input("How many stars?"))
for i in range(0,star_number):
    print("*", end="")

"""

star_number = int(input("How many stars?"))
line_number = 1
for j in range(star_number):
    for i in range(line_number):
        print("*", end="")
    print()
    line_number += 1
