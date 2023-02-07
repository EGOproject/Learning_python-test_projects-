#credit youtube @ tech with tim
import random 

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

COLS = 3
ROWS = 3

symbol_count = {
    
}
def deposit ():
    while True:
        amount = input("DEPOSIT: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Number of lines to BET on\n\n[1-1-3]??\n\n")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter number.")
    return lines

def get_bet():
    while True:
        amount = input("What's your BET: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(F"Amount must be between ${[MIN_BET]} - ${[MAX_BET]}.")
        else:
            print("Please enter number.")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You canot bet more than your balance which is: [${balance}]")
        else:
            break
    print(f"Your are betting ${[bet]} on {[lines]} lines. your total bet is: ${total_bet}")

main()
