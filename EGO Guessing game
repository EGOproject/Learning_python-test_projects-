#this is a number guessing game


import random

print("WELCOME TO EGO GUESSING GAME")
print()
print("How many Rounds do you need to play this game")
playing_rounds = int(input("Playing Rounds: "))

def human_guess():
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
    print("Thank you for trying our guessing game. Goodbye!!😎")

round_loop()
