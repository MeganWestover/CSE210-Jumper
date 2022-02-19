class Guesser:
    '''Counts how many matches the user guesses.'''
    def __init__(self):
        pass

    def search_letter(self,guessword,letter):
        lettertimes = guessword.count(letter)

        if lettertimes == 0:
            guess = False
        else:
            guess = True

        return guess