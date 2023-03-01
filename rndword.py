import random

class rndword:
    def __init__(self) -> None:
        self.word_count = { #length : count
            5 : 15920,
            6 : 29874,
            7 : 41998,
            8 : 51627
        }
        self.used_words = { i : [] for i in range(5,9) }
        
    def generate_id(self, word_len : int) -> int:
        """get a uniqe id for a word in file
        Args: word_len (int): the length of the wanted word (5 - 8)
        Returns: int: id (line) of word in file
        """
        while True:
            word_id = random.randint(0, self.word_count[word_len]) - 1
            if not (word_id in self.used_words[word_len]):
                self.used_words[word_len].append(word_id)
                return word_id
 
    def generate_word(self, word_len : int = None) -> str :
        """get a uniqe word
        Args: word_len (int, optional): wanted length of word (5 - 8). Defaults to random.
        Returns: str: new word from file
        """
        if not word_len: 
            word_len = random.randint(5,8)
        word_id = self.generate_id(word_len)
        
        with open(f"words\\words_{word_len}.txt", "r") as file:
            file.seek((word_len + 2) * word_id)
            word = file.read(word_len)
        
        return word
    