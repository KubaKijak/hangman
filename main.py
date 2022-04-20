

import random 
import tkinter as tk

root = tk.Tk()
root.title ("Hangman")
window_width = 500
window_height = 400


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)


root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

def salect_word(game):
    file = open ("file.txt", "r+")
    word_guess = random.choice(file.read().split())
    file.close 
    return word_guess


def guess_word( word ):
    player_guess = []
    for i in  word:
        player_guess.append("_")

    tries = 8

    while (tries > 0):
        print()

    print(word)
    print(player_guess)

    
word_guess = salect_word("file.txt")
print(word_guess)

root.mainloop()