from calc_class import Calculations
from classes import Options

option = Options.op()


def u_input():
    if option == 1:
        state = "added to"
    elif option == 2:
        state = "subtracted from"
    elif option == 3:
        state = "multiplied by"
    elif option == 4:
        state = "divided by"
    num1 = input("First number: ")
    print(f"\n[{num1}] {state} ...")
    num2 = input("Second number: ")
    return num1, num2

def op_dir():
    if option == 1:
        print("\nEnter Numbers to add....... ")
        u_input()
        result = Calculations.addition(num1, num2)
        print(f"\nThe [SUM] is: [{result}]")
    

    elif option == 2:
        print("\nEnter Numbers to subtract....... ")
        u_input()
        result = Calculations.subtraction(num1, num2)
        print(f"\nThe [DIFFERENCE] is: [{result}]")

    elif option == 3:
        print("\nEnter Numbers to multiply....... ")
        u_input()
        result = Calculations.multiplication(num1, num2)
        print(f"\nThe [PRODUCT] is: [{result}]")
    

    elif option == 4:
        print("\nEnter Numbers to divide....... ")
        u_input()
        result = Calculations.division(num1, num2)
        print(f"\nThe [QUOTIENT] is: [{result}]")


op_dir()