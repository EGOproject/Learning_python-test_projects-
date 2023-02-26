# my personalized continuation module

def ctn():
    tu = 0
    while tu >= 0:
        if tu == 0:
            print("\nWELCOME TO ....... !!") # welcome to name of program
            # place the function of continuation here ie.... game()
            tu += 1
        else:
            tu += 1
            a = [ "y", "n"]
            choice = input("CONTINUE ?\n[Y/N]?? : ").lower() # Customizable string in quotes. DO YOU WANT TO MAKE ANOTHER LIST?
            while choice not in  a:
                print("try again")
                choice = input("CONTINUE ?\n[Y/N]?? : ").lower() # Customizable string in quotes. DO YOU WANT TO MAKE ANOTHER LIST?
                if choice == "y" or "n":
                    break
                else:
                    exit()
            if choice == "y":
                # place the function of continuation here ie.... game()
                pass # pass is a place holder. delete this line if function is placed above
            elif choice == "n":
                if (tu - 1) > 1:
                    print(f"\nYOU HAVE USED [## program name] TO MAKE [{tu - 1}] -----!!\n") # programa name inserted there ---- program functionality
                    break
                elif (tu - 1) == 1:
                    print(f"\nYOU HAVE USED [## program name] TO MAKE [{tu - 1}] -----!!\n") # programa name inserted there ----- program functionality
                    break
ctn()