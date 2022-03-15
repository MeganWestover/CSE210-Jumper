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