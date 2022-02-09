import random


# def main():

#     words = []

#     append_random_words(words)
#     print(f"raundwords: {words}")

#     append_random_words(words, 5)
#     print(f"raundwords: {words}")


# def append_random_words(word_list, quantity=1):
#     list_of_words = [
#         "arm",
#         "car",
#         "cloud",
#         "head",
#         "heal",
#         "hydrogen",
#         "jog",
#         "join",
#         "laugh",
#         "love",
#         "sleep",
#         "smile",
#         "speak",
#         "sunshine",
#         "toothbrush",
#         "tree",
#         "truth",
#         "walk",
#         "water",
#     ]
#     for _ in range(quantity):
#         random_words = random.choice(list_of_words)
#         word_list.append(random_words)


# # Call main to start this program.
# if __name__ == "__main__":
#     main()


def choose_words():
    list_of_words = [
        "arm",
        "car",
        "cloud",
        "head",
        "heal",
        "hydrogen",
    ]
    word = random.choice(list_of_words)
    return word


def track_guesses(word, gusses):
    letters = ""
    for letter in word:
        if letter in gusses:
            letters += letter
        else:
            letters = "*"
    return letters


def handle_guess(word):
    gussed_letters = []
    chances = len(word) * 2
    print(f"Find a word that is {len(word)} letters long")

    while True:
        if chances != 0:
            print(f"Words so far: {track_guesses(word, gusses)} ")
            guess = input("Guess: ")[0]
            if guess != gussed_letters:
                gussed_letters.append(guess)


while True:
    word = choose_words()
    handle_guess(word)
    if input("Would you like to continue ").lower().startswith("n"):
        break
