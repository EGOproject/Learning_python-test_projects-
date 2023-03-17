#this is a number guessing game developed by EGOproject


import random

def ctu():
    def hg():
        print("User mode 👤")
        min = int(input("Enter first boundary: " ))
        max = int(input("Enter second boundary: "))
        rn = random.randint(min, max)
        g = 0
        gr = 0
        while g != rn:
            g = int(input(f"\nEnter your Guess between {min} and {max}\n\nYour Guess:"))
            gr = gr + 1
            if g > rn:
                print(f"Sorry, Try LOWER. Number of guesses is: {gr}")
            elif g < rn:
                print(f"Sorry, Try HIGHER. Number of guesses is: {gr}")
        print(f"\n🎉🎊 Congratulations!!, You have guessed the right number as [{rn}] in {gr} Guess(es)!!🎊🎉")

    def rl():
        rp = 0
        rdn =0
        while rp != pr:
            rp= rp + 1
            rdn = rdn + 1
            print()
            print(f"ROUND [ {rdn} ]!! START 🤩")
            hg()
        print()
        print("Thank you for trying our guessing game. Goodbye!!😎\nTry the new computer mode and try wider ranges in any mode you like!!")

    rl()

def utc():
    def cg():
        print("Computer mode 💻")
        min = int(input("Enter first boundary: " ))
        max = int(input("Enter second boundary: "))
        uf = ""
        gr = 0
        while uf != "c":
            gr = gr + 1
            if min == max:
                rn == min == max
                print(f"My guess is: {rn} \n\n[C]...I Am Correct!\n[H]...Try Higher\n[L]...Try Lower")
                break
            elif min==max-1 or max==min+1:
                rn = min or max 
                print(f"My guess is: {rn} \n\n[C]...I Am Correct!\n[H]...Try Higher\n[L]...Try Lower")
            elif min != max:
                rn = random.randint(min, max)
                print()
                print(f"My guess is: {rn} \n\n[C]...I Am Correct!\n[H]...Try Higher\n[L]...Try Lower")
                uf = input("\n[C/H/L]??:").lower()
                if uf == "l":
                    max = rn
                elif uf == "h":
                    min = rn
            
            
        print()
        print(f"\n🎉🎊 Hooray!!, I have guessed the right number as [{rn}] in {gr} Guess(es)!!🎊🎉")

    def rl():
        rp=0
        rdn =0
        while rp != pr:
            rp= rp + 1
            rdn = rdn + 1
            print()
            print(f"ROUND [ {rdn} ]!! START 🤩")
            cg()
        print()
        print("Thank you for trying our guessing game. Goodbye!!😎\nTry the user mode and try wider ranges in any mode you like!!")

    rl()

print("WELCOME TO EGO GUESSING GAME")
print()
print("How many Rounds do you need to play this game")
print()
pr = int(input("Playing Rounds: "))

print("\nWho is going to guess in this game?\nUser [U]\nComputer[c]\n\n[U/C]??")
print()
m = input("Mode: ").lower()
if m == "c":
    utc()
elif m == "u":
    ctu()  
else:
    print()
    print("Wrong input try restarting the game...")
    exit()
exit()   
# this is the key to all variable abbreviations
# the importance was to summarize the code

"""
    utc - user testing computer
    ctu - computer testing user
    hg - human_guess
    min - minimum
    max - maximum
    rn - random_number
    g - guess
    gr - guess_rounds
    rl - round_loop
    rp - rounds_played
    pr - playing_rounds
    rdn - round_number
    cg - computer_guess
    uf - user_feedback
    m - mode

"""