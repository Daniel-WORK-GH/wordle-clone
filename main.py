import os
import time
import color_print
import validator
import rndword

class wordle:
    def __init__(self, word_len = 5, max_tries = 5) -> None:
        self.word_generator = rndword.rndword()
        self.word_len = word_len
        self.max_guesses = max_tries
        self.curret_word = None
        self.guesses = []

    def generate_word(self):
        self.curret_word = self.word_generator.generate_word(self.word_len)
    
    def guess_word(self, guess : str) -> bool:
        if len(guess) != len(self.curret_word):
            return False
        if not validator.validate_word(guess):
            return False
        self.guesses.append(guess)
        return True

    def check_winloss(self) -> str:
        if len(self.guesses) == 0:
            return 'ONGOING'
        if self.curret_word == self.guesses[len(self.guesses) - 1]:
            return 'WON'
        if len(self.guesses) == self.max_guesses:
            return 'LOST'
        return 'ONGOING'

    def update(self):
        self.generate_word()
        mode = 'ONGOING'
        self.guesses = []

        while mode == 'ONGOING':            
            self.draw()
            guess = input('enter word : ')
            os.system('cls')
            if not self.guess_word(guess):
                color_print.print_colored("invalid word", color_print.red)
            mode = self.check_winloss()
        self.draw()

        if mode == 'LOST':
            print(f'the word was : {self.curret_word}')
        if mode == 'WON':
            print(f'good job! the word was {self.curret_word}')
        
    def draw(self):
        print('word length :', self.word_len, end=", ")
        print('guesses left :', self.max_guesses - len(self.guesses))
        for x in self.guesses:
            letters = list(self.curret_word)
            guess_letters = list(x)
            for i, j in zip(letters, guess_letters):
                if j == i:
                    color_print.print_colored(j, color_print.green, end='')
                elif j in letters:
                    color_print.print_colored(j, color_print.yellow, end='')
                else:
                    color_print.print_colored(j, color_print.red, end='')
            print()

def get_word_len() -> int:
    word_len = 0    
    while True:
        word_len = input("enter word length (5 - 8) : ")
        os.system('cls')
        if not word_len.isdecimal():
            color_print.print_colored("invalid input (string)", color_print.red)
            continue
        word_len = int(word_len)
        if 5 > word_len or word_len > 8:
            color_print.print_colored("invalid input (range)", color_print.red)
            continue
        break
    return word_len
    
os.system('cls')
play_again = True

while play_again:
    word_len = get_word_len()
    game = wordle(word_len)
    os.system('cls')
    game.update()
    play_again = input("play again ? (y/n)") == "y"