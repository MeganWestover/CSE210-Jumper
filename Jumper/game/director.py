from game.guesser import Guesser
from game.word_array import WordArray
from game.terminal_service import TerminalService



class Director: 
    '''Class that directs the game. Initiates game play
    and makes it flow the way it should.'''
    def __init__(self):
        
        self._wordarray = WordArray()
        self.is_playing = True
        self._guesser = Guesser()
        self._terminal_service = TerminalService()
        self.numberofguesses = 0
        self.guessedletters = []

    def start_game(self):
        '''Starts the game by running the maingame loop'''
        
        self._terminal_service.write_text("Welcome to the jump game!!!!")
        print("_ _ _ _ _")
        while self.is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        '''It shows to the user the fields of the word to be guessed, and asks him to guess a letter.'''
        
        self.word_space = self._wordarray.get_wordlenght()
        self.word_slected = self._wordarray.get_wordselected()
        self.new_letter = self._terminal_service.read_text("Guess a letter [a-z]: ")
    
    def _do_updates(self):
        '''Find if the letter guessed by user is in the guess word and Keeps track of guesses'''
        self.guess = self._guesser.search_letter(self.word_slected,self.new_letter)
        if self.guess == False:
            self.numberofguesses += 1
        else:
            if self.numberofguesses == 0:
                self.numberofguesses = 0
                self.guessedletters.append(self.new_letter)
            else:
                self.numberofguesses += -1
                self.guessedletters.append(self.new_letter)

    def _do_outputs(self):
        '''Shows the parachute modification according to the update data and displays the letters guessed by user if apply'''
        continuegame = self._terminal_service.draw_parachute(self.word_slected,self.guessedletters,self.word_space,self.guess,self.numberofguesses)
        if continuegame == False:
            self.is_playing = False
        else:
            self.is_playing = True
