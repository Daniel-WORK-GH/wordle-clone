#HACK should use seek and binary search

def validate_word(word : str) -> bool :
    with open(f"words\\words_{len(word)}.txt") as file:
        current_word = file.readline().strip('\n')
        while word >= current_word:
            if current_word == word:
                return True           
            current_word = file.readline().strip('\n')
    return False

