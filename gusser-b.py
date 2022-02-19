import random

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


# Another Try on the gusser class
# from array import array
import random


class Guesser:
    def __init__(self):
        pass

        self._location = random.choice(word_array)
        self._distance = [0, 0]

        def get_hint(self):
            message = "Way off target"
            if self._distance[-1] == 0:
                message = "Good job you found it"
            elif self._distance[-1] > self._distance[-2]:
                message = "Guess again"
            elif self._distance[-1] < self._distance[-2]:
                message = "Getting closer! guess again"
            return message

        def word_found(self):
            return self._distance[-1] == 0
