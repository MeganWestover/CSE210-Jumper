# from array import array
import random

from Jumper import WordArray


class Guesser:
    def __init__(self):
        pass
        self._words = WordArray
        self._location = random.choice()
        # self._distance = [0, 0]

        def get_hint(self):
            # message = "Way off target"
            if self._distance[-1] == 0:
                message = "Good job you found it"
            elif self._distance[-1] > self._distance[-2]:
                message = "Guess again"
            elif self._distance[-1] < self._distance[-2]:
                message = "Getting closer! guess again"
            return message

        def word_found(self):
            return self._distance[-1] == 0
