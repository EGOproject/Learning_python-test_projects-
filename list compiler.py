# this is a list compiler program designed in python using vsCode
import time

def lm():
    ln = input("\nName the List: ").upper()
    mi = int(input("\nEnter number of items: "))
    il = []

    while len(il) < mi:
        ni = input(f"\nAdd new item to {ln} : ").upper()
        if ni not in il:
                il.append(ni)
                il.sort()
                time.sleep(0.5)
                print(f"\nList Count: [{len(il)}], Left with [{mi - len(il)}]")
                print(", ".join(il))
        elif ni in il:
            print(f"{ni} already exists on {ln} list")
    time.sleep(5)
    print(f"\nCollected the {mi} items on the {ln} list below:\n")
    print(f"{ln} List:")
    for index, char in enumerate(il):
        print(f"{index+1} - {char}")
    print()

def ctn():
    tu = 0
    while tu >= 0:
        if tu == 0:
            print("\nWELCOME TO THE LIST MAKER!!")
            lm()
            tu += 1
        else:
            tu += 1
            a = [ "y", "n"]
            choice = input("DO YOU WANT TO MAKE ANOTHER LIST?\n[Y/N]?? : ").lower()
            while choice not in  a:
                print("try again")
                choice = input("DO YOU WANT TO MAKE ANOTHER LIST?\n[Y/N]?? : ").lower()
                if choice == "y" or "n":
                    break
                else:
                    exit()
            if choice == "y":
                lm()
            elif choice == "n":
                if (tu - 1) > 1:
                    print(f"\nYOU HAVE USED LIST MAKER TO MAKE [{tu - 1}] LISTS!!\n")
                    break
                elif (tu - 1) == 1:
                    print(f"\nYOU HAVE USED LIST MAKER TO MAKE [{tu - 1}] LIST!!\n")
                    break

ctn()