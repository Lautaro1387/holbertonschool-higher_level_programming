#!/usr/bin/python3
"""class name: Base"""


import json


class Base:
    """class name: Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            Base.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """The JSON string representation of list_objs"""
        if list_objs is None:
            list_objs = []

