@@ -1,38 +0,0 @@
# Used to derive multiples of any number

def multiples():
    ntbm = int(input("\nNumber to be multiplied: "))
    mnom = int(input("\nMaximum number of Multiples: "))
    mn = 0
    print(f"\n\nThese are [{mnom}] multiples of [{ntbm}]\n")
    while mn != mnom:
        mn += 1
        result = ntbm * mn
        print(f"[{ntbm} X {mn}] = {result}\n")

def ctn():
    tu = 0
    while tu >= 0:
        if tu == 0:
            print("\nWELCOME TO THE MULTIPLE DERIVER!!")
            multiples()
            tu += 1
        else:
            tu += 1
            a = [ "y", "n"]
            choice = input("DO YOU WANT TO CONTINUE?\n[Y/N]?? : ").lower()
            while choice not in  a:
                print("try again")
                choice = input("DO YOU WANT TO CONTINUE?\n[Y/N]?? : ").lower()
                if choice == "y" or "n":
                    break
                else:
                    exit()
            if choice == "y":
                multiples()
            elif choice == "n":
                print(f"\nYOU HAVE USED EMD [{tu}] times!!\n")
                exit()

ctn()
                    
