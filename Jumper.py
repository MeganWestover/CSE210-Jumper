import string
import random

class Director: 
    '''Class that directs the game. Initiates game play
    and makes it flow the way it should.'''
    def __init__(self):
        
        self._wordarray = WordArray()
        self.is_playing = True
        self._guesser = Guesser()
        self._terminal_service = TerminalService()
        self.numberofguesses = 0
        self.worddisplayed = []

    def start_game(self):
        '''Starts the game by running the maingame loop'''
        
        self._terminal_service.write_text("Welcome to the jump game!!!!")
        while self.is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        '''It shows to the user the fields of the word to be guessed, and asks him to guess a letter.'''
        
        self.word_space = self._wordarray.get_wordlenght()
        print(self.word_space)
        self.word_slected = self._wordarray.get_wordselected()
        print(self.word_slected)
        self.worddisplayed = self._wordarray.get_worddisplayed()
        print(self.worddisplayed)
        self.new_letter = self._terminal_service.read_text("Guess a letter [a-z]: ")
    
    def _do_updates(self):
        '''Find if the letter guessed by user is in the guess word and Keeps track of guesses'''
        self.guess = self._guesser.search_letter(self.word_slected,self.new_letter)
        if self.guess == False:
            self.numberofguesses += 1
        else:
            if self.numberofguesses == 0:
                self.numberofguesses = 0
            #else:
                #self.numberofguesses += -1
        print(self.numberofguesses)

    def _do_outputs(self):
        '''Shows the parachute modification according to the update data and displays the letters guessed by user if apply'''
        continuegame = self._terminal_service.draw_parachute(self.word_slected,self.new_letter,self.word_space,self.guess,self.numberofguesses)
        if continuegame == False:
            self.is_playing = False
        else:
            self.is_playing = True

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

'''class GameBoard:
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
        print()'''

class TerminalService:
    """This class helps us handle terminal operations"""

    def __init__(self):
        '''Constructs an empty list to save the word to be guessed'''
        self.hideword = []

    def write_stripes(self,wordlenght,list):
        '''displays first horizontal stripes for each letter of the word to be guessed'''
        for i in range(wordlenght):
            print("_",end=" "),
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
        """Displays the given text on the terminal. 

        """
        print(text)

    def draw_parachute(self,guessword,letter,wordlenght,guess,number_of_guesses):
        '''displays the word guessing status and the parachute situation'''
    
        i = 0
        self.hideword = list(guessword)
        if guess:
            for i in range(wordlenght):
                if letter == guessword[i]:
                    print(letter,end=" "),
                else:
                    print("_",end=" "),
            print(" \n")
            
            cont = True
        else:
            for i in range(wordlenght):
                print("_",end=" "),
            print(" \n")

        if number_of_guesses == 0:
            print('  ___  ')
            print(' /___\ ')
            print(' \   / ')
            print('  \ /  ')
            print('   O   ')
            print('  /|\  ')
            print('  / \  ')
            print()
            print('^^^^^^^')
            print()
            cont = True
        elif number_of_guesses == 1:
            print(' /___\ ')
            print(' \   / ')
            print('  \ /  ')
            print('   O   ')
            print('  /|\  ')
            print('  / \  ')
            print()
            print('^^^^^^^')
            print()
            cont = True
        elif number_of_guesses == 2:
            print(' \   / ')
            print('  \ /  ')
            print('   O   ')
            print('  /|\  ')
            print('  / \  ')
            print()
            print('^^^^^^^')
            print()
            cont = True
        elif number_of_guesses == 3:
            print('  \ /  ')
            print('   O   ')
            print('  /|\  ')
            print('  / \  ')
            print()
            print('^^^^^^^')
            print()
            cont = True
        elif number_of_guesses == 4:
            print('   x   ')
            print('  /|\  ')
            print('  / \  ')
            print()
            print('^^^^^^^')
            print()
            print('Oh no your parachute is missing!! Game Over')
            cont = False
        
        return cont


class WordArray:
    def __init__(self):
        self._array = ["Hello", "Shire", "Bring", "Acorn", "Please", "Close", "Front", "Frame", "Zebra", "Libra", "Speed", "Creed", "Anime", "Silly", "Smart", "Crazy", "Learn", "Stern", "Koala", "Brand", "Stand",  "Happy", "Style", "Miles", "Arrow", "Drama", "Allow", "Apply", "Child", "Crime", "Dress", "Dream", "Drink", "Enemy", "Entry", "Focus", "Fruit", "Glass", "Green", "Group", "Heart", "Guide", "Jones", "Judge", "Knife", "Layer", "March", "Major", "Metal", "Money", "Month", "Motor", "Music", "Panel", "Owner", "North", "Night", "Plane", "Plant", "Point", "Power", "Reply", "River", "Round", "Route", "Rugby", "Scale", "Scene", "Shape", "Smoke", "Sound", "South", "Space", "Sport", "Stock"]
        self._wordselected = random.choice(self._array)
        self._wordlenght = len(self._wordselected)
        self._worddisplayed = []

    def get_wordselected(self):
        self._wordselected = self._wordselected.lower()
        return self._wordselected
    def get_wordlenght(self):
        return self._wordlenght
    def get_worddisplayed(self):
        self._worddisplayed = list(self._wordselected)
        i=0
        for _ in (self._worddisplayed):
            self._worddisplayed[i] = "_"
            i += 1
        return self._worddisplayed
    
    


def main():
    director = Director()
    director.start_game()


if __name__ == "__main__":
    main()