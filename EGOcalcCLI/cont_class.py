# my personalized continuation module
import main_calc

class Continuation:
    def __init__(self):
        pass

    def ctn():
        tu = 0
        while tu >= 0:
            if tu == 0:
                print("Welcome to CLI EGOcalc")
                print("================================ ")
                main_calc.calc
                tu += 1
            else:
                tu += 1
                a = [ "y", "n"]
                choice = input("CONTINUE ?\n[Y/N]?? : ").lower()
                while choice not in  a:
                    print("Try again")
                    choice = input("CONTINUE ?\n[Y/N]?? : ").lower()
                    if choice == "y" or "n":
                        break
                    else:
                        exit()
                if choice == "y":
                    main_calc.calc
                    pass
                elif choice == "n":
                    if (tu - 1) > 1:
                        print(f"\nYOU HAVE USED [CLI EGOcalc] TO MAKE [{tu - 1}] Calculations!!\n")
                        break
                    elif (tu - 1) == 1:
                        print(f"\nYOU HAVE USED [CLI EGOcalc] TO MAKE [{tu - 1}] Calculation!!\n")
                        break
    ctn()