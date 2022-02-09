import random


def main():

    words = []

    append_random_words(words)
    print(f"raundwords: {words}")

    append_random_words(words, 5)
    print(f"raundwords: {words}")


def append_random_words(word_list, quantity=1):
    list_of_words = [
        "arm",
        "car",
        "cloud",
        "head",
        "heal",
        "hydrogen",
        "jog",
        "join",
        "laugh",
        "love",
        "sleep",
        "smile",
        "speak",
        "sunshine",
        "toothbrush",
        "tree",
        "truth",
        "walk",
        "water",
    ]
    for _ in range(quantity):
        random_words = random.choice(list_of_words)
        word_list.append(random_words)


# Call main to start this program.
if __name__ == "__main__":
    main()
