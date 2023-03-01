# Wordle-clone

python based wordle game,
the list of words used are taken from https://github.com/dwyl/english-words

### About the game
original word - randomly generated word of length n

the objective is to guess the original word
each time you need you need to write a word of the same lengeth
and gather enough clues to guess the correctly

for every letter in the word you guessed it will be colored : 
- red if its not in the original word
- yellow if its in the original word but its not in the correct place
- green if its in the original word and in the correct place

for example : 

![example 1](https://user-images.githubusercontent.com/120199463/222119217-b392d309-b755-4a0d-9b3a-dbd94903a125.png)



### technical data 
the original word can be only of length 5 - 8 characters
the default nubmer of tries is 5 but it can be changed with a small change to the code

color_print can use 256 colors, based on : https://stackabuse.com/how-to-print-colored-text-in-python/

file_creator was used only to separate word of length 5-8 from the original file

rnd_word generates a random uniqe word of length n, the same word wont be generated 
twice in the same run, only after reset

validator checks if an entered word is valid (is in the list of words) so the player cant write gibberish 
