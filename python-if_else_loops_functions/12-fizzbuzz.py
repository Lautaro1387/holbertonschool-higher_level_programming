#!/usr/bin/python3
def fizzbuzz():
    for test in range(1, 101):
        if test % 3 == 0 and test % 5 == 0:
            print("FizzBuzz", end=" ")
        elif test % 3 == 0:
            print("Fizz", end=" ")
        elif test % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(test), end=" ")
