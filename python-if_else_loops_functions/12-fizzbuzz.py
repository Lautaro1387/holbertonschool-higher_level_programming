#!/usr/bin/python3
for test in range (1, 100):
    if test % 3 == 0 and test % 5 == 0:
        print("FizzBuzz", end=" ")
    elif test % 3 == 0:
        print("Fizz", end=" ")
    elif test % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(f"{test}", end=" ")
if test != 100:
    print("", end="")
    
