#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lastDigit = abs(number) % 10
output = "last digit of {} is {}".format(number, lastDigit)

if lastDigit > 5:
    print(output + " and is greater than 5")
elif lastDigit == 0:
    print(output + " and is 0")
else:
    print(output + " and is less than 6 and not 0")
