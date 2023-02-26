# this is a list compiler program designed in python using vsCode
import time
          

def lm():
    ln = input("\nName the List: ").upper()
    mi = int(input("\nEnter number of items: "))
    il = []
    dil = []
    def atl():
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
            else:
                print("WTF this ain't even possible")
    atl()
    def em():
        a =[ "y", "n"]
        tu = 0
        def dem ():
            itd = input("\nItem to delete: ").upper()
            if itd in il:
                il.remove(itd)
                dil.append(itd)
                print(f"\n{itd} deleted from {ln} list successfully!!")
                print(f"\nList Count: [{len(il)}], Left with [{mi - len(il)}]")
                print(", ".join(il))
            else:
                while itd not in il:
                    if itd not in (il and dil):
                        itd = input(f"\nTRY AGAIN !! {itd} not on {ln} List!!\nItem to delete: ").upper()
                    elif itd in dil:
                        itd = input(f"\nTRY AGAIN !! {itd} already [DELETED] from {ln} List!!\nItem to delete: ").upper()
                il.remove(itd)
                dil.append(itd)
                print(f"\n{itd} deleted from {ln} list successfully!!")
                print(f"\nList Count: [{len(il)}], Left with [{mi - len(il)}]")
                print(", ".join(il))
        while tu >= 0:
            if tu == 0:
                print("\nEDIT MODE!!")               
                tu += 1
                dem()
            else:
                tu += 1
                a = [ "y", "n"]
                choice = input("\nContinue Editing?\n[Y/N]?? : ").lower()
                while choice not in  a:
                    print("try again")
                    choice = input("\nContinue Editing?\n[Y/N]?? : ").lower()
                    if choice == "y" or "n":
                        break

                if choice == "y":
                    dem()
                elif choice == "n":
                    if (tu - 1) > 1:
                        print(f"\nYou have made [{tu - 1}] EDITS!!\n")
                        break
                    elif (tu - 1) == 1:
                        print(f"\nYou have made [{tu - 1}] EDIT!!\n")
                        break
    
    emc = input(f"\nDo you need to [DELETE] any item in the {ln} list above? [ Y /N ]?? : ").lower()
    a = ["y", "n"]
    if emc in a:
        if emc=="y":
            em()
        elif emc=="n":
            print(f"\nThis is the final {ln} list")
        else:
            while emc not in a:
                emc = input(f"\nDo you need to [DELETE] any item in the {ln} list above? [ Y /N ]?? : ").lower()
    admctn = input("Replace Deleted Items? [ Y / N ]?? : ").lower()
    if  admctn in a:
        if admctn=="y":
            atl()
        elif admctn=="n":
            pass
        else:
            while admctn not in a:
                admctn = input(f"\nDo you need to [REPLACE] the deleted items in {ln} list above? [ Y /N ]?? : ").lower()
    time.sleep(5)
    print(f"\nCollected the {len(il)} items on the {ln} list below:\n")
    print(f"{ln} List:")
    for index, char in enumerate(il):
        print(f"{index+1} - {char}")
    print()
    print(f"\nDeleted the {len(dil)} items from the {ln} list above:\n")
    print(f"Deleted items List:")
    for index, char in enumerate(dil):
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