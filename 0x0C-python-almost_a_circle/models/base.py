#!/usr/bin/python3
"""
Base class
"""
import json


class Base:
    """
    Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        with public attribute id
        :param id:
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file"""
        for i in (list_objs):
            dic_1 = i.to_dictionary()

            name = i.__class__.__name__ + ".json"
            with open(name, "w") as f:
                f.write(cls.to_json_string(dic_1))
