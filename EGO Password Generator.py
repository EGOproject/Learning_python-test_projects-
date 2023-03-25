#this is a password generator by EGOsoft
#Credits: Harshit Bhai - The HackerxGuy

import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"
symbols = "!@#$%/\<>?:"
pform = upper + lower + number + symbols

def gen():
    while 1 == 1:
        try:
            plen = int(input("\nPassword length Requied: "))
        except TypeError and ValueError:
            print("Invalid password length")
        else:
            break

    password = []

    while plen < 8:
        try:
            plen = int(input("\nPassword length Required [Minimum: 8]: "))
        except TypeError and ValueError:
            print("Invalid password length")
        

    while plen > len(password):
            pchar = random.choice(pform)
            password.append(pchar)
    
    print(f"\nGenerated password: ", "".join(password))


def ctn():
    tu = 0
    while tu >= 0:
        if tu == 0:
            print("\nWELCOME TO EGO password Generator !!")
            gen()
            tu += 1
        else:
            tu += 1
            a = [ "y", "n"]
            choice = input("CONTINUE ?\n[Y/N]?? : ").lower() 
            while choice not in  a:
                print("try again")
                choice = input("CONTINUE ?\n[Y/N]?? : ").lower()
            if choice == "y":
                gen()
            elif choice == "n":
                if (tu - 1) > 1:
                    print(f"\nYOU HAVE USED [EGO Password Generator] TO MAKE [{tu - 1}] Passwords!!\n")
                    break
                elif (tu - 1) == 1:
                    print(f"\nYOU HAVE USED [EGO Password Generator] TO MAKE [{tu - 1}] Password!!\n")
                    break
ctn()