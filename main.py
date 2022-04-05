

import random 

def salect_word(game):
    file = open ("file.txt", "r+")
    word_guess = random.choice(file.read().split())
    file.close 
    return word_guess
    
word_guess = salect_word("file.txt")
print(word_guess)