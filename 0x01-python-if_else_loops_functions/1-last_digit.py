#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lastDigit = abs(number) % 10
output = "last digit of {} is {} and is ".format(number, lastDigit)

if lastDigit > 5:
    print(output + "greater than 5")
elif lastDigit == 0:
    print(output + "0")
else:
    print(output + "less than 6 and not 0")
