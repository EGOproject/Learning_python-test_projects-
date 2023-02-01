#this is a number guessing game developed by EGOproject


import random

def ctu():
    def human_guess():
        print("User mode 👤")
        first_boundary = int(input("Enter first boundary: " ))
        second_boundary = int(input("Enter second boundary: "))
        random_number = random.randint(first_boundary, second_boundary)
        guess = 0
        guess_rounds = 0
        while guess != random_number:
            guess = int(input(f"\nEnter your Guess between {first_boundary} and {second_boundary}\n\nYour Guess:"))
            guess_rounds = guess_rounds + 1
            if guess > random_number:
                print(f"Sorry, Try LOWER. Number of guesses is: {guess_rounds}")
            elif guess < random_number:
                print(f"Sorry, Try HIGHER. Number of guesses is: {guess_rounds}")
        print(f"\n🎉🎊 Congratulations!!, You have guessed the right number as [{random_number}] in {guess_rounds} Guess(es)!!🎊🎉")

    def round_loop():
        rounds_played=0
        round_number =0
        while rounds_played != playing_rounds:
            rounds_played= rounds_played + 1
            round_number = round_number + 1
            print()
            print(f"ROUND [ {round_number} ]!! START 🤩")
            human_guess()
        print()
        print("Thank you for trying our guessing game. Goodbye!!😎\nTry the new computer mode and try wider ranges in any mode you like!!")

    round_loop()

def utc():
    def computer_guess():
        print("Computer mode 💻")
        first_boundary = int(input("Enter first boundary: " ))
        second_boundary = int(input("Enter second boundary: "))
        user_feedback=""
        guess_rounds = 0
        while user_feedback != "c":
            guess_rounds = guess_rounds + 1
            if first_boundary != second_boundary:
                random_number = random.randint(first_boundary, second_boundary)
                print()
                print(f"My guess is: {random_number} \n\n[C]...I Am Correct!\n[H]...Try Higher\n[L]...Try Lower")
                user_feedback = input("\n[C/H/L]??:").lower()
                if user_feedback == "l":
                    second_boundary = random_number - 1
                elif user_feedback == "h":
                    first_boundary = random_number + 1
            else:
                random_number = first_boundary or second_boundary 
                print(f"My guess is: {random_number} \n\n[C]...I Am Correct!\n[H]...Try Higher\n[L]...Try Lower") 
        print()
        print(f"\n🎉🎊 Hooray!!, I have guessed the right number as [{random_number}] in {guess_rounds} Guess(es)!!🎊🎉")

    def round_loop():
        rounds_played=0
        round_number =0
        while rounds_played != playing_rounds:
            rounds_played= rounds_played + 1
            round_number = round_number + 1
            print()
            print(f"ROUND [ {round_number} ]!! START 🤩")
            computer_guess()
        print()
        print("Thank you for trying our guessing game. Goodbye!!😎\nTry the user mode and try wider ranges in any mode you like!!")

    round_loop()

print("WELCOME TO EGO GUESSING GAME")
print()
print("How many Rounds do you need to play this game")
print()
playing_rounds = int(input("Playing Rounds: "))

print("\nWho is going to guess in this game?\nUser [U]\nComputer[c]\n\n[U/C]??")
print()
mode = input("Mode: ").lower()
if mode == "c":
    utc()
elif mode == "u":
    ctu()  
else:
    print()
    print("Wrong input try restarting the game...")
    exit()
exit()   