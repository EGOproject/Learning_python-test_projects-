# This is a Rock, Paper, Scissors game

import random
def rpsg():
    def rm():
        print("⭕⭕ROUND MODE!!⭕⭕")
        def rps():
            uf = input("[R]---Rock\n[P]---Paper\n[S]---Scissors\n\nYour CHOICE: ").lower()
            cc = random.choice(["r","p","s"])
            #allocating computer choice to an actual string the user can undrstand
            if cc == "r":
                ccv = "Rocks"
            elif cc == "p":
                ccv = "Paper"
            else:
                ccv = "Scissors"

            if uf == cc:
                print(f"It's a Tie, I chose: {ccv}")
            elif (uf == "r" and cc == "s") or(uf == "s" and cc == "p") or(uf == "p" and cc == "r"):
                print(f"🎉🎊Congratulations!! You have WON!!🎊🎉 I chose: {ccv}")
            elif (cc == "r" and uf == "s") or (cc == "s" and uf == "p") or (cc == "p" and uf == "r"):
                print(f"😔💔You have lost!! Next time Better💔😔 I chose: {ccv}")

        def rl():
            print("How many Rounds do you need to play this game")
            print()
            pr = int(input("Playing Rounds: "))
            rp=0
            rdn =0
            while rp != pr:
                rp= rp + 1
                rdn = rdn + 1
                print()
                print(f"ROUND [ {rdn} ]!! START 🤩")
                rps()
            print()
            print("Try out the unlimited mode!!")
            print("Thank you for trying our ROCK PAPER SCISSORS game. Goodbye!!😎")
        rl()

    def um():
        print("🔁🔁UNLIMITED MODE🔁🔁")
        def rps():
            uf = input("[R]---Rock\n[P]---Paper\n[S]---Scissors\n[E]---EXIT\n\nYour CHOICE: ").lower()
            cc = random.choice(["r","p","s"])
            #allocating computer choice to an actual string the user can undrstand
            if cc == "r":
                ccv = "Rocks"
            elif cc == "p":
                ccv = "Paper"
            else:
                ccv = "Scissors"

            if uf == cc:
                print(f"It's a Tie, I chose: {ccv}")
            elif (uf == "r" and cc == "s") or(uf == "s" and cc == "p") or(uf == "p" and cc == "r"):
                print(f"🎉🎊Congratulations!! You have WON!!🎊🎉 I chose: {ccv}")
            elif (cc == "r" and uf == "s") or (cc == "s" and uf == "p") or (cc == "p" and uf == "r"):
                print(f"😔💔You have lost!! Next time Better💔😔 I chose: {ccv}")
            elif uf == "e":
                print("Try the round mode to challenge your self with the computer!!")
                print("Thank you for trying our ROCK PAPER SCISSORS game. Goodbye!!😎")
                exit()
            else:
                print(f"Round WASTED, Stop CHEATING!!\n\n[{uf}] IS NOT AN OPTION!! Try Again")
        def ul():
            rp = 0
            while 1 == 1:
                print()
                rp = rp + 1
                print(f"ROUND [ {rp} ]!! START 🤩")
                rps()
            return "What does 1 == to now??"
        ul()



    print("WELCOME TO EGO ROCK PAPER SCISSORS GAME")
    print()
    print("Which mode do you need to play?? \n\n**ROUND MODE ------ Set the number of rounds you want to play, normally for competition.\n**UNLIMITED MODE -- play unlimited times.")
    print()
    print("[1] --- Round Mode\n[2] --- Unlimited Mode\n\n[1/2]??")
    print()
    m = int(input("Mode: "))
    if m == 1:
        rm()
    elif m == 2:
        um()  
    else:
        print()
        print("Wrong input try restarting the game...")
        exit()
    exit()

def drg():
    def rm():
        print("⭕⭕ROUND MODE!!⭕⭕")
        def dr():
            rc = input("\n[1]---ONE ⚪\n[2]---TWO ⚪⚪\n[3]---THREE ⚪⚪⚪\n[4]---FOUR ⚪⚪⚪⚪\n[5]---FIVE ⚪⚪⚪⚪⚪\n[6]---SIX ⚪⚪⚪⚪⚪⚪\n\nROLL[Y/N]: ").lower()
            uf = random.choice([1,2,3,4,5,6])
            cc = random.choice([1,2,3,4,5,6])
            #allocating computer choice to an actual string the user can undrstand
            if cc == 1:
                ccv = "ONE ⚪"
            elif cc == 2:
                ccv = "TWO ⚪⚪"
            elif cc == 3:
                ccv = "THREE ⚪⚪⚪"
            elif cc == 4:
                ccv = "FOUR ⚪⚪⚪⚪"
            elif cc == 5:
                ccv = "FIVE ⚪⚪⚪⚪⚪"
            elif cc == 6:
                ccv = "SIX ⚪⚪⚪⚪⚪⚪"
            
            #allocating user choice to an actual string the user can undrstand
            if uf == 1:
                ucv = "ONE ⚪"
            elif uf == 2:
                ucv = "TWO ⚪⚪"
            elif uf == 3:
                ucv = "THREE ⚪⚪⚪"
            elif uf == 4:
                ucv = "FOUR ⚪⚪⚪⚪"
            elif uf == 5:
                ucv = "FIVE ⚪⚪⚪⚪⚪"
            elif uf == 6:
                ucv = "SIX ⚪⚪⚪⚪⚪⚪"

            if rc == "y":
                if uf == cc:
                    print(f"It's a Tie, WE both Rolled: {ccv}")
                elif uf > cc and uf <= 6:
                    print(f"🎉🎊Congratulations!! You have WON!!🎊🎉 You Rolled: {ucv} I Rolled: {ccv}")
                elif cc > uf and uf >= 1:
                    print(f"😔💔You have lost!! Next time Better💔😔 You Rolled: {ucv} I Rolled: {ccv}")
                else:
                    print(f"Round WASTED, Stop CHEATING!!\n\n[{uf}] IS NOT AN OPTION!! Try Again")
            else:
                print("Thank you for trying our DICE ROLL game. Goodbye!!😎")
                exit()

        def rl():
            print("How many Rounds do you need to play this game")
            print()
            pr = int(input("Playing Rounds: "))
            rp=0
            rdn =0
            while rp != pr:
                rp= rp + 1
                rdn = rdn + 1
                print()
                print(f"ROUND [ {rdn} ]!! START 🤩")
                dr()
            print()
            print("Thank you for trying our DICE ROLL game. Goodbye!!😎")
        rl()

    def um():
        print("🔁🔁UNLIMITED MODE🔁🔁")
        def dr():
            rc = (input("\n[1]---ONE ⚪\n[2]---TWO ⚪⚪\n[3]---THREE ⚪⚪⚪\n[4]---FOUR ⚪⚪⚪⚪\n[5]---FIVE ⚪⚪⚪⚪⚪\n[6]---SIX ⚪⚪⚪⚪⚪⚪\n\nROLL[Y/N]: ")).lower()
            uf = random.choice([1,2,3,4,5,6])
            cc = random.choice([1,2,3,4,5,6])
            #allocating computer choice to an actual string the user can undrstand
            if cc == 1:
                ccv = "ONE ⚪"
            elif cc == 2:
                ccv = "TWO ⚪⚪"
            elif cc == 3:
                ccv = "THREE ⚪⚪⚪"
            elif cc == 4:
                ccv = "FOUR ⚪⚪⚪⚪"
            elif cc == 5:
                ccv = "FIVE ⚪⚪⚪⚪⚪"
            else:
                ccv = "SIX ⚪⚪⚪⚪⚪⚪"
            
            #allocating user choice to an actual string the user can undrstand
            if uf == 1:
                ucv = "ONE ⚪"
            elif uf == 2:
                ucv = "TWO ⚪⚪"
            elif uf == 3:
                ucv = "THREE ⚪⚪⚪"
            elif uf == 4:
                ucv = "FOUR ⚪⚪⚪⚪"
            elif uf == 5:
                ucv = "FIVE ⚪⚪⚪⚪⚪"
            elif uf == 6:
                ucv = "SIX ⚪⚪⚪⚪⚪⚪"

            if rc == "y":
                if uf == cc:
                    print(f"It's a Tie, WE both Rolled: {ccv}")
                elif uf > cc and uf <= 6:
                    print(f"🎉🎊Congratulations!! You have WON!!🎊🎉 You Rolled: {ucv} I Rolled: {ccv}")
                elif cc > uf and uf >= 1:
                    print(f"😔💔You have lost!! Next time Better💔😔 You Rolled: {ucv} I Rolled: {ccv}")
                else:
                    print(f"Round WASTED, Stop CHEATING!!\n\n[{uf}] IS NOT AN OPTION!! Try Again")
            else:
                print("Thank you for trying our DICE ROLL game. Goodbye!!😎")
                exit()
        def ul():
            rp = 0
            while 1 == 1:
                print()
                rp = rp + 1
                print(f"ROUND [ {rp} ]!! START 🤩")
                dr()
            return "What does 1 == to now??"
        ul()



    print("WELCOME TO EGO ROCK PAPER SCISSORS GAME")
    print()
    print("Which mode do you need to play?? \n\n**ROUND MODE ------ Set the number of rounds you want to play, normally for competition.\n**UNLIMITED MODE -- play unlimited times.")
    print()
    print("[1] --- Round Mode\n[2] --- Unlimited Mode\n\n[1/2]??")
    print()
    m = int(input("Mode: "))
    if m == 1:
        rm()
    elif m == 2:
        um()  
    else:
        print()
        print("Wrong input try restarting the game...")
        exit()
    exit()

print("WELCOME TO EGO ROCK PAPER SCISSORS and DICE ROLL GAME")
print()
print("Which GAME do you need to play?? \n\n**PLAY ROCK PAPER SCISSORS.\n**PLAY DICE ROLL.")
print()
print("[1] --- ROCK PAPER SCISSORS\n[2] --- DICE ROLL\n\n[1/2]??")
print()
gm = int(input("Game Mode: "))
if gm == 1:
    rpsg()
elif gm == 2:
    drg()  
else:
    print()
    print("Wrong input try restarting the game...")
    exit()

# this is the key to all variable abbreviations
# the importance was to summarize the code

"""
    rpsg - rock_paper_scissors_game
    rps - rock_paper_scissors
    drg - dice_roll_game
    dr - dice_roll
    gm - game_mode
    rp - rounds_played
    pr - playing_rounds
    rdn - round_number
    cc - computer_choice
    uf - user_feedback
    rm - round_mode
    rl - round_loop
    um - unlimited_mode
    ul - unlimited_loop
    cca - computer_choice_allocation
    ccv - computer_choice_value
    cucva - computer_and_user_choice_value_allocation
    ucv - user_choice_value
"""