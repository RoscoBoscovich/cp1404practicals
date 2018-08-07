"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
not_finished = True
while not_finished == True:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
        not_finished = False
    except ValueError:
     print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
     print("Please enter a non-zero number")
print("Finished.")