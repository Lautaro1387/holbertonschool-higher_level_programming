#!/usr/bin/python3
def uppercase(str):
    for str2 in str:
        str2 = ord(str2)
        if str2 > 96 and str2 < 123:
            str2 = str2 - 32
        print("{:c}".format(str2), end="")
    print()
