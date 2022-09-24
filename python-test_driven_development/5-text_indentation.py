#!/usr/bin/python3
"""Prints a text with 2 new lines aftereach of there characters"""


def text_indentation(text):
    """def name: text_indentation"""
    if text is not str:
        raise TypeError("text must be a string")
    print("{}".format(text),end="")
