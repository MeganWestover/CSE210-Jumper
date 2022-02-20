"""

Authors: Megan Westover, Brandon Luce, Camilo Camargo, Richard Asare

Jumper/Parachute/Hang Man game

"""

import string
import random


class Director:
    """Class that directs the game. Initiates game play
    and makes it flow the way it should."""

    def __init__(self):

        self._wordArray = WordArray()
        self.is_playing = True
        self._guesser = Guesser()
        self._terminal_service = TerminalService()
        self.numberOfGuesses = 0
        self.guessedLetters = []

    def start_game(self):
        """During game play the director does inputs, updates, and outputs."""
        self._terminal_service.write_text("Welcome to the jump game!!!!")
        print("_ _ _ _ _")
        while self.is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """It shows to the user the fields of the word to be guessed, and asks him to guess a letter."""

        self.word_space = self._wordArray.get_wordLength()
        self.word_selected = self._wordArray.get_wordSelected()
        self.new_letter = self._terminal_service.read_text("Guess a letter [a-z]: ")

    def _do_updates(self):
        """Find if the letter guessed by user is in the guess word and Keeps track of guesses"""
        self.guess = self._guesser.search_letter(self.word_selected, self.new_letter)
        if self.guess == False:
            self.numberOfGuesses += 1
        else:
            if self.numberOfGuesses == 0:
                self.numberOfGuesses = 0
                self.guessedLetters.append(self.new_letter)
            else:
                self.numberOfGuesses += -1
                self.guessedLetters.append(self.new_letter)

    def _do_outputs(self):
        """Shows the parachute modification according to the update data and displays the letters guessed by user if apply"""
        continueGame = self._terminal_service.draw_parachute(
            self.word_selected,
            self.guessedLetters,
            self.word_space,
            self.guess,
            self.numberOfGuesses,
        )
        if continueGame == False:
            self.is_playing = False
        else:
            self.is_playing = True


class Guesser:
    """Counts how many matches the user guesses."""

    def __init__(self):
        pass

    def search_letter(self, guessWord, letter):
        letterTimes = guessWord.count(letter)

        if letterTimes == 0:
            guess = False
        else:
            guess = True

        return guess


class TerminalService:
    """This class helps us handle terminal operations"""

    def __init__(self):
        """Constructs an empty list to save the word to be guessed"""
        self.hideWord = []

    def write_stripes(self, wordLength, list):
        """displays first horizontal stripes for each letter of the word to be guessed"""
        for i in range(wordLength):
            print("_", end=" "),
        print(" \n")

    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.
        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def read_number(self, prompt):
        """Gets numerical input from the terminal. Directs the user with the given prompt.
        Returns:
            float: The user's input as a number.
        """
        return float(input(prompt))

    def write_text(self, text):
        """Displays the given text on the terminal."""
        print(text)

    def draw_parachute(self, guessWord, letter, wordLength, guess, number_of_guesses):
        """displays the word guessing status and the parachute situation"""

        i = 0
        k = 0
        for _ in guessWord:
            if guessWord[i] in letter:
                print(guessWord[i], end=" "),
                a = guessWord.count(guessWord[i])
                if a > 1:
                    k += 1
                else:
                    k += 1
            else:
                print("_", end=" "),
            i += 1
        print(" \n")

        if k == len(guessWord):
            print("  ___  ")
            print(" /___\ ")
            print(" \   / ")
            print("  \ /  ")
            print("   O   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
            print()
            print("Congrats you have won!!!!")
            exit()

        if number_of_guesses == 0:
            print("  ___  ")
            print(" /___\ ")
            print(" \   / ")
            print("  \ /  ")
            print("   O   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
            print()
            cont = True
        elif number_of_guesses == 1:
            print("    _  ")
            print(" /___\ ")
            print(" \   / ")
            print("  \ /  ")
            print("   O   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
            print()
            cont = True
        elif number_of_guesses == 2:
            print(" /___\ ")
            print(" \   / ")
            print("  \ /  ")
            print("   O   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
            print()
            cont = True
        elif number_of_guesses == 3:
            print("   __\ ")
            print(" \   / ")
            print("  \ /  ")
            print("   O   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
            print()
            cont = True
        elif number_of_guesses == 4:
            print(" \   / ")
            print("  \ /  ")
            print("   O   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
            print()
            cont = True
        elif number_of_guesses == 5:
            print("     / ")
            print("  \ /  ")
            print("   O   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
            print()
            cont = True
        elif number_of_guesses == 6:
            print("  \ /  ")
            print("   O   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
            print()
            cont = True
        elif number_of_guesses == 7:
            print("    /  ")
            print("   O   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
            print()
            cont = True
        elif number_of_guesses == 8:
            print("   x   ")
            print("  /|\  ")
            print("  / \  ")
            print()
            print("^^^^^^^")
            print()
            print("Oh no your parachute is missing!! Game Over")
            cont = False

        return cont


class WordArray:
    def __init__(self):
        self._array = [
            "Hello",
            "Shire",
            "Bring",
            "Acorn",
            "Please",
            "Close",
            "Front",
            "Frame",
            "Zebra",
            "Libra",
            "Speed",
            "Creed",
            "Anime",
            "Silly",
            "Smart",
            "Crazy",
            "Learn",
            "Stern",
            "Koala",
            "Brand",
            "Stand",
            "Happy",
            "Style",
            "Miles",
            "Arrow",
            "Drama",
            "Allow",
            "Apply",
            "Child",
            "Crime",
            "Dress",
            "Dream",
            "Drink",
            "Enemy",
            "Entry",
            "Focus",
            "Fruit",
            "Glass",
            "Green",
            "Group",
            "Heart",
            "Guide",
            "Jones",
            "Judge",
            "Knife",
            "Layer",
            "March",
            "Major",
            "Metal",
            "Money",
            "Month",
            "Motor",
            "Music",
            "Panel",
            "Owner",
            "North",
            "Night",
            "Plane",
            "Plant",
            "Point",
            "Power",
            "Reply",
            "River",
            "Round",
            "Route",
            "Rugby",
            "Scale",
            "Scene",
            "Shape",
            "Smoke",
            "Sound",
            "South",
            "Space",
            "Sport",
            "Stock",
        ]
        self._wordSelected = random.choice(self._array)
        self._wordLength = len(self._wordSelected)
        self._wordDisplayed = []

    def get_wordSelected(self):
        self._wordSelected = self._wordSelected.lower()
        return self._wordSelected

    def get_wordLength(self):
        return self._wordLength

    def get_wordDisplayed(self):
        self._wordDisplayed = list(self._wordSelected)
        i = 0
        for _ in self._wordDisplayed:
            self._wordDisplayed[i] = "_"
            i += 1
        return self._wordDisplayed


def main():
    director = Director()
    director.start_game()


if __name__ == "__main__":
    main()
