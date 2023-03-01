# used to fix words list from https://github.com/dwyl/english-words
# take words with only 5 <= letters <= 8

# a lot of strange words left but its just an example
# so we'll keep them for now

def gen_readline():
    with open("words\\old_words.txt", "r") as file:
        while True:
            line = file.readline().strip('\n')
            if line == '': break
            yield line

def sort_file():
    lines : list
    with open("words\\old_words.txt", "r") as file:
        lines = file.readlines()
        lines.sort()
    with open("words\\old_words.txt", "w") as file:
        for l in lines:
            file.write(l)
            
def create_files():
    gen = gen_readline()
    files = [
        open(f"words\\words_{i}.txt", "w") for i in range(5, 9)
    ]

    for w in gen:
        if 5 <= len(w) <= 8:
            files[len(w) - 5].write(w + '\n')

    for x in files:
        x.close()

#sort_file() 
#create_files()