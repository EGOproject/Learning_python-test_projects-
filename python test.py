# qyestion 1

name = "john"

# question 2
age = 30
print(type(age))
# the type is integer (int)

#question 3
salary = 5000.50

# question 4
print(2+3*4)
# the output is 14

# question 5
6/ 2 == 3

# question 6

def rectangle_area():

    length = 4
    width = 5
    area = length * width

    print(area)
rectangle_area()


# question 7

def check_even_number():
    number = int(input("Please enter a number to check: "))

    if number%2 == 0:
        print(f"{[number]} is an Even number.")
    else:
        print(f"{[number]} is not an Even number.")

check_even_number()

# question 8

def age_comment():
    age = int(input("How old are you? : "))

    if age >= 18:
        print("You are OLD enough!!")
    else:
        print("You are not OLD enough!!")

age_comment()

# question 9

def sum():
    print()
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter second number: "))

    sum = first_number + second_number

    print(f"FOr: {[first_number]} + {[second_number]}")
    print(f"The SUM is: {[sum]}")

sum()

# question 10
import random
def greet():
    greetings = [
        "How are you ",
        "Hello ",
        "Hi ",
        "How is your day "
            ]
    name = input("What is your name? : ")
    rand_greet = random.choice(greetings)

    print(rand_greet + name)

greet()


    



