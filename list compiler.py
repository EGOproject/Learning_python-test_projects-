# this is a list compiler program designed in python using vsCode
import time
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)

def lm():
    pyttsx3.speak("Name the List")
    ln = input("\nName the List: ").upper()
    pyttsx3.speak("Enter maximum number of items")
    mi = int(input("\nEnter number of items: "))
    il = []
    dil = []
    def atl():
        while len(il) < mi:
            # pyttsx3.speak(f"Add new item to {ln}")
            ni = input(f"\nAdd new item to {ln} : ").upper()
            if ni not in il:
                    il.append(ni)
                    il.sort()
                    time.sleep(0.5)
                    pyttsx3.speak(f"\nList Count: [{len(il)}], Left with [{mi - len(il)}]")
                    print(f"\nList Count: [{len(il)}], Left with [{mi - len(il)}]")
                    print(", ".join(il))
            elif ni in il:
                pyttsx3.speak(f"{ni} already exists on {ln} list")
                print(f"{ni} already exists on {ln} list")
            else:
                pyttsx3.speak("What The Fuck!, This ain't even possible!")
                print("WTF this ain't even possible")
    atl()
    def em():
        a =[ "y", "n"]
        tu = 0
        def dem ():
            pyttsx3.speak("Insert item to delete!")
            itd = input("\nItem to delete: ").upper()
            if itd in il:
                il.remove(itd)
                dil.append(itd)
                pyttsx3.speak(f"{itd} deleted from {ln} list successfully!!")
                print(f"\n{itd} deleted from {ln} list successfully!!")
                pyttsx3.speak(f"List Count: {len(il)}, Left with {mi - len(il)}")
                print(f"\nList Count: [{len(il)}], Left with [{mi - len(il)}]")
                print(", ".join(il))
            else:
                while itd not in il:
                    if itd not in (il and dil):
                        pyttsx3.speak(f"TRY AGAIN !! {itd} not on {ln} List. INSERT Item to delete: ")
                        itd = input(f"\nTRY AGAIN !! {itd} not on {ln} List!!\nItem to delete: ").upper()
                    elif itd in dil:
                        pyttsx3.speak(f"TRY AGAIN !! {itd} already [DELETED] from {ln} List. INSERT Item to delete: ")
                        itd = input(f"\nTRY AGAIN !! {itd} already [DELETED] from {ln} List!!\nItem to delete: ").upper()
                il.remove(itd)
                dil.append(itd)
                pyttsx3.speak(f"{itd} IS SUCCESSFULLY deleted from {ln} list.")
                print(f"\n{itd} deleted from {ln} list successfully!!")
                pyttsx3.speak(f"\nList Count: [{len(il)}], Left with [{mi - len(il)}]")
                print(f"\nList Count: [{len(il)}], Left with [{mi - len(il)}]")
                print(", ".join(il))
        while tu >= 0:
            if tu == 0:
                pyttsx3.speak("EDIT MODE!!")
                print("\nEDIT MODE!!")               
                tu += 1
                dem()
            else:
                tu += 1
                a = [ "y", "n"]
                pyttsx3.speak("do you need to continue editing?")
                choice = input("\nContinue Editing?\n[Y/N]?? : ").lower()
                while choice not in  a:
                    pyttsx3.speak("please try again")
                    print("try again")
                    pyttsx3.speak("do you need to continue editing?")
                    choice = input("\nContinue Editing?\n[Y/N]?? : ").lower()
                    if choice == "y" or "n":
                        break

                if choice == "y":
                    dem()
                elif choice == "n":
                    if (tu - 1) > 1:
                        pyttsx3.speak(f"You have made [{tu - 1}] EDITS!!")
                        print(f"\nYou have made [{tu - 1}] EDITS!!\n")
                        break
                    elif (tu - 1) == 1:
                        pyttsx3.speak(f"You have made [{tu - 1}] EDIT!!")
                        print(f"\nYou have made [{tu - 1}] EDIT!!\n")
                        break
    
    pyttsx3.speak(f"Do you need to [DELETE] any item in the {ln} list above?")
    emc = input(f"\nDo you need to [DELETE] any item in the {ln} list above? [ Y /N ]?? : ").lower()
    a = ["y", "n"]
    if emc in a:
        if emc=="y":
            em()
        elif emc=="n":
            pyttsx3.speak(f"This is the final {ln} list")
            print(f"\nThis is the final {ln} list")
        else:
            while emc not in a:
                pyttsx3.speak(f"Do you need to [DELETE] any item in the {ln} list above?")
                emc = input(f"\nDo you need to [DELETE] any item in the {ln} list above? [ Y /N ]?? : ").lower()
    pyttsx3.speak("do you need to replace the items you have deleted?")
    admctn = input("Replace Deleted Items? [ Y / N ]?? : ").lower()
    if  admctn in a:
        if admctn=="y":
            atl()
        elif admctn=="n":
            pass
        else:
            while admctn not in a:
                pyttsx3.speak(f"Do you need to [REPLACE] the items you deleted in {ln} list above?")
                admctn = input(f"\nDo you need to [REPLACE] the deleted items in {ln} list above? [ Y /N ]?? : ").lower()
    time.sleep(5)
    pyttsx3.speak(f"Collected the {len(il)} items on the {ln} list below:")
    print(f"\nCollected the {len(il)} items on the {ln} list below:\n")
    pyttsx3.speak(f"Below, is the final {ln} List:")
    print(f"{ln} List:")
    for index, char in enumerate(il):
        print(f"{index+1} - {char}")
    print()
    pyttsx3.speak(f"you deleted {len(dil)} items from the {ln} list above")
    print(f"\nDeleted the {len(dil)} items from the {ln} list above:\n")
    pyttsx3.speak("these are the items you deleted")
    print(f"Deleted items List:")
    for index, char in enumerate(dil):
        print(f"{index+1} - {char}")
    print()

def ctn():
    tu = 0
    while tu >= 0:
        if tu == 0:
            pyttsx3.speak("WELCOME TO THE LIST MAKER!!")
            print("\nWELCOME TO THE LIST MAKER!!")
            lm()
            tu += 1
        else:
            tu += 1
            a = [ "y", "n"]
            pyttsx3.speak("DO YOU WANT TO MAKE ANOTHER LIST?")
            choice = input("DO YOU WANT TO MAKE ANOTHER LIST?\n[Y/N]?? : ").lower()
            while choice not in  a:
                pyttsx3.speak("try again")
                print("try again")
                pyttsx3.speak("DO YOU WANT TO MAKE ANOTHER LIST?")
                choice = input("DO YOU WANT TO MAKE ANOTHER LIST?\n[Y/N]?? : ").lower()
                if choice == "y" or "n":
                    break
                else:
                    exit()
            if choice == "y":
                lm()
            elif choice == "n":
                if (tu - 1) > 1:
                    pyttsx3.speak(f"YOU HAVE USED LIST MAKER TO MAKE [{tu - 1}] LISTS")
                    print(f"\nYOU HAVE USED LIST MAKER TO MAKE [{tu - 1}] LISTS!!\n")
                    break
                elif (tu - 1) == 1:
                    pyttsx3.speak(f"YOU HAVE USED LIST MAKER TO MAKE [{tu - 1}] LIST")
                    print(f"\nYOU HAVE USED LIST MAKER TO MAKE [{tu - 1}] LIST!!\n")
                    break
time.sleep(5)
ctn()