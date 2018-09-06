
"""
CP1404/CP5632 Practical
Counts occurrences of words in a text string.
"""


def main():
    # sentence = input("Text:")
    sentence = "zebra xylophone apple orange apple zebra cup candle cup cup candle zebra xylophone"

    word_list = sentence.split()

    word_count_dict = {}

    for word in word_list:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1

    key_list = []
    max_key_length = 0
    for key, val in word_count_dict.items():
        key_list.append(key)
        max_key_length = len(key) if len(key) > max_key_length else max_key_length
    key_list.sort()

    print("Text: {}:".format(sentence))
    for key in key_list:
        print("{:{m_l}} : {}".format(key, word_count_dict[key], m_l=max_key_length))


main()
