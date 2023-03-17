# these are the classes being used in the project

class Options:
    def __init__(self, option):
        self.option = option
    
    def op():
        functions = ["1.Addition", "2.Subtraction", "3.Multiplication", "4.Division", "5.Powers", "6.Roots"]
        print("\nCHOOSE THE OPERATION YOU WOULD LIKE TO USE!!")
        print("================================ ")
        print()
        for operation in functions:
            print(operation, sep = "\n")
        print("             [1,2,3,4,5,6]??")
        option = int(input("OPTION: "))
        print("================================ ")
        return option
