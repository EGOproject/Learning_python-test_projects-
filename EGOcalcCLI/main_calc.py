from calc_class import Calculations

print("\nWelcome to the CLI EGOcalc")
print()

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

sum = Calculations.addition(num1, num2)

print(sum)