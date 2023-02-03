# This is a hangman games codeed in python
# the logic is that users have to guess the letters in the random word selected from the list up to completion.
# https://github.com/EGOproject
import random
import string
from lib import wcs

ul=0
def svw(wcs):
    ws = random.choice(wcs)
    while (" " in wcs) or ("-" in wcs):
        ws = random.choice(wcs)
    return ws.upper()

def hmg():        
    ws = svw(wcs)
    liw = set(ws)
    abc = set(string.ascii_uppercase)
    agl = set()
    ul = 10
    rds = 0
    pts = 0
    # input from users to guess and the game loop
    while len(liw) > 0 and ul > 0:
        rds = rds + 1
        pts = 15 - rds
        print(f"\nYou have {ul} lives left!!\n\nLetters gussed so far: ", " ".join(agl))     # " ".join(["a","b", "cd"]) --> "a b cd"
        glfo = [letter if letter in agl else "_" for letter in ws]      # This makes something like this " L--T-R "
        print("Your WORD so far: ", " ".join(glfo))
        ung = input("Guess a letter: ").upper()
        # logic for keeping track of the letters keyed in by the users
        if ung in abc - agl: #the "-" means and not in
            agl.add(ung)
            if ung in liw:
                liw.remove(ung)
            else:
                ul = ul - 1
                print("\n--------------------------------------\n--------------------------------------\nLetter NOT in word!! You LOST a LIFE")
        elif ung in agl - liw:
            print("\n\nYou have already guessed the letter and more of it is nolonger necessary for the word you are guessing!!\nPlease try AGAIN!!")
        else:
            print("\n\nINVALID LETTER!!\nPlease try AGAIN!!")
    if ul == 0:
        print(f"\nYou DIED!! The WORD was: {ws}")
    elif len(liw) == 0:
        print(f"\nCongratulations!! You have GUESSED your word as: ", " ".join(ws), f"\n\nYour points are: [{pts}].", )
        
print("\n\n-----------------------------------------------------------------------------------------------------")
print("WELCOME TO THE EGO HANGMAN GAME!!\n")
hmg()
print("\nThank you for playing our hangman game!! visit https:///github.com/EGOproject")
print("\n\n-----------------------------------------------------------------------------------------------------")

# key for abbreviated variable names in the code
"""
    lib - library
    wcs - word_choices
    svw - select_valid_word
    hmg - hangman_game
    ws - word_selected
    liw - letters_in_word
    abc - alphabets
    agl - already_guessed_letters
    ung - user's_new_guess
    glfo - guessed_list_for_output
    ul - user_lives
    rds - rounds
    pts - points
"""