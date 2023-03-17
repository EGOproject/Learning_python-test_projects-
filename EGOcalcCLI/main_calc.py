from calc_class import Calculations

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


def u_input():
    option = op().option
    if op() == 1:
        state = "added to"
    elif op() == 2:
        state = "subtracted from"
    elif op() == 3:
        state = "multiplied by"
    elif op() == 4:
        state = "divided by"
    num1 = input("First number: ")
    print(f"\n[{num1}] {state} ...")
    num2 = input("Second number: ")
    return num1, num2

def op_dir():
    if op() == 1:
        print("\nEnter Numbers to add....... ")
        u_input()
        result = Calculations.addition(num1, num2)
        print(f"\nThe [SUM] is: [{result}]")
    

    elif op() == 2:
        print("\nEnter Numbers to subtract....... ")
        u_input()
        result = Calculations.subtraction(num1, num2)
        print(f"\nThe [DIFFERENCE] is: [{result}]")

    elif op() == 3:
        print("\nEnter Numbers to multiply....... ")
        u_input()
        result = Calculations.multiplication(num1, num2)
        print(f"\nThe [PRODUCT] is: [{result}]")
    

    elif op() == 4:
        print("\nEnter Numbers to divide....... ")
        u_input()
        result = Calculations.division(num1, num2)
        print(f"\nThe [QUOTIENT] is: [{result}]")


op_dir()