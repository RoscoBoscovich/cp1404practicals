"""
CP1404/CP5632 - Practical
Random word generator - based on format of words
Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""

def word_gen_main():
    import random

    VOWELS = "aeiou"
    CONSONANTS = "bcdfghjklmnpqrstvwxyz"

    word_format = input("""Please enter sting for word generator""")
    validity = is_valid_format(word_format)

    if validity == False:
        print("Invalid input!")

    while validity == True:

        word = ""
        for kind in word_format:
              if kind == "c":
                 word += random.choice(CONSONANTS)
              else:
                 word += random.choice(VOWELS)
        validity = False
        print(word)



def is_valid_format(word_format):
    for kind in word_format:
        if (kind == "c") or (kind == "v"):
            valid_flag = True
        else:
            return False
    return valid_flag


word_gen_main()