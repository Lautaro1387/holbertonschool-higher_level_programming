#!/usr/bin/python3
"""Prints a text with 2 new lines aftereach of there characters"""


def text_indentation(text):
    """def name: text_indentation"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for delimit in ".?:":
        text = (delimit + "\n\n").join(
            [line.strip(" ") for line in text.split(delimit)])
    print("{}".format(text), end="")
