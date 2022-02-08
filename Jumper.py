import string

class Director: 
    '''Class that directs the game. Initiates game play
    and makes it flow the way it should.'''
    def __init__(self):
        self.is_playing = True
        self._wordarray = WordArray()
        self._guesser = Guesser()
        self._terminal_service = TerminalService()

    def start_game(self):
        '''During game play the director does inputs, updates, and outputs.'''
        while self.is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        '''Reads letter.'''
        new_letter = self._terminal_service.read_letter("/nGuess a letter [a-z]: ")

    
    def _do_updates(self):
        '''Keeps track of guesses'''
        
    def _do_outputs(self):
        hint = self._wordarray.


class Guesser:
    def __init__():
        pass

class GameBoard:
    def __init__():
        pass
    def GameBoard(board):
        print('  ___  ')
        print(' /___\\')
        print(' \\   / ')
        print('  \\ /  ')
        print('   0   ')
        print('  /|\\ ')
        print('  / \\ ')
        print()
        print('^^^^^^^')
        print()

class TerminalService():
    def __init__():
        pass


class WordArray:
    def __init__(self):
        pass

    def Array(self):
        self.array = ["Hello", "Shire", "Bring", "Acorn", "Please", "Close", "Front", "Frame", "Zebra", "Libra", "Speed", "Creed", "Anime", "Silly", "Smart", "Crazy", "Learn", "Stern", "Koala", "Brand", "Stand",  "Happy", "Style", "Miles", "Arrow", "Drama", "Allow", "Apply", "Child", "Crime", "Dress", "Dream", "Drink", "Enemy", "Entry", "Focus", "Fruit", "Glass", "Green", "Group", "Heart", "Guide", "Jones", "Judge", "Knife", "Layer", "March", "Major", "Metal", "Money", "Month", "Motor", "Music", "Panel", "Owner", "North", "Night", "Plane", "Plant", "Point", "Power", "Reply", "River", "Round", "Route", "Rugby", "Scale", "Scene", "Shape", "Smoke", "Sound", "South", "Space", "Sport", "Stock"]

def main():
    director = Director()
    director.start_game()


if __name__ == "__main__":
    main()