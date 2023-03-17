# this is a CLI calculator by EGOproject
# credit: EGOproject

import math


class Calculations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(num1, num2):
        sum = num1 + num2
        return sum

    def subtraction(num1, num2):
        difference = num1 - num2
        return difference

    def multiplication(num1, num2):
        product = num1 * num2
        return product

    def division(num1, num2):
        quotient = num1 / num2
        return quotient

    def powered_number(num1, num2):
        p_ans = math.pow(num1, num2)
        return p_ans

    def roots(num1, num2):
        if num2 == 2:
            s_root = math.sqrt(num1)
            return s_root
        elif num2 == 3:
            c_root = math.cbrt
            return c_root
        else:
            print("Wrong number of roots")

        