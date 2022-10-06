#!/usr/bin/python3
"""class name: Base"""


import json
from os import path


class Base:
    """class name: Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            Base.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file doc"""
        new_list = []
        name = str(cls.__name__) + ".json"
        with open(name, 'w', encoding='utf8') as f:
            if list_objs is None:
                f.write(cls.to_json_string(new_list))
            else:
                for obj in list_objs:
                    new_list.append(cls.to_dictionary(obj))
                f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == []:
            json_string = []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load_from_file doc"""
        l_instances = []
        if path.isfile(f"{cls.__name__}.json"):
            with open(f"{cls.__name__}.json", 'r') as f:
                for line in f:
                    instances = cls.from_json_string(line)
                    for item in instances:
                        l_instances.append(cls.create(**item))
        return l_instances
