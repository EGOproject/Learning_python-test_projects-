#thi is a prime number program

prime_numbers = []

lower = int(input("Lower value: "))
upper = int(input("Upper value: "))

for number in range(lower, upper+1):
    if number > 1:
          for i in range(2,number):
               if (number%i) == 0:
                    break
          else:
               if number not in prime_numbers:
                    prime_numbers.append(number)
               else:
                    break


print(prime_numbers)