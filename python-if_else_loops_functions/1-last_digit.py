#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = random.randint(-10, 10)
if last_digit != 0:
    if number > 5:
        print(f"Last digit of {number} is {last_digit} and is greater than 5")
    elif number == 0:
        print(f"Last digit of {number} is {last_digit} and is 0")
    elif number < 6 != 0:
        print(f"Last diigt of {number} is {last_digit} and is less than 6 and not 0")
