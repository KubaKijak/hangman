
import random
from resource import display_hangman


def salect_word():    # Dena def kallar på text.txt filen där det finns ord till spelet 
    file = open ("file.txt", "r+")
    word = random.choice(file.read().split())
    file.close 
    return word.upper()
    #word = random.choice(word_list)
    #return word.upper()



def play(word):
    """Denna def är huvudspelet och här finns kod för hur koden avgör om ordet är korrekt.
     Det finns funktioner för att avgöra om bokstaven är skriven korreket annars rättas den 
    till korrekt form eller så frågas man att gissa om.
    Args:
        word (_type_): _description_
    """
                             
    word_guess= "_" * len(word)
    guessed = False                    
    guessed_letter = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))

    print(word_guess)
    print("\n")

    while not guessed and tries > 0:
        player_guess = input("guess letter: ") .upper()
        if len(player_guess) == 1 and player_guess.isalpha():
            if player_guess in guessed_letter:
                print("you already used that letter", player_guess)
            elif player_guess not in word:
                print(player_guess, "is not the right letter in the word")
                tries -= 1
                guessed_letter.append(player_guess)
            else:
                print("The letter,", player_guess, "is in the world")
                guessed_letter.append(player_guess)
                word_to_list = list(word_guess)
                index = [i for i, letter in enumerate(word) if letter == player_guess]
                for index2 in index: 
                    word_to_list[index2] = player_guess
                    word_guess = "".join(word_to_list)
                    if "_" not in word_guess:
                        guessed = True
        elif len(player_guess) == len(word) and player_guess.isalpha():
            if player_guess in guessed_words:
                print ("you already used that word", player_guess)
            elif player_guess != word:
                print(player_guess, "is not the word")
                tries -= 1
                guessed_words.append(player_guess)
            else: 
                guessed = True 
                word_guess = word 
        else:
            print("You are not following the rules")
        print(display_hangman(tries))
        print(word_guess)
        print("\n")
    if guessed:
        print("congrats, you win")
    else:
        print("sorry, but you lost. the word was " + word + ".")


def main():    
    """Här spelas spelet upp och så kan man välja att spela igen 
    """
    word = salect_word()
    play(word)
    while input("do you want to play again(Y/N)").upper()== "Y":
        word = salect_word()
        play(word)

if __name__ == "__main__":
    main()
