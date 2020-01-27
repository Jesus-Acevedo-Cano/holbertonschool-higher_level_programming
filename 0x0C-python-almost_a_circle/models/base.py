#!/usr/bin/python3
""" base class"""
import json
import csv


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ list dictionaries to JSON string """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string representation to a file """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write('[]')
            else:
                _dict = [dic.to_dictionary() for dic in list_objs]
                file.write(cls.to_json_string(_dict))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ list of instances """
        fileno = cls.__name__ + ".json"
        try:
            with open(fileno, "r") as file:
                lists = Base.from_json_string(file.read())
                return [cls.create(**nlist) for nlist in lists]
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes and deserializes in CSV """
        csvNew = cls.__name__ + ".csv"
        with open(csvNew, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Square":
                    attribs = ["id", "size", "x", "y"]
                else:
                    attribs = ["id", "width", "height", "x", "y"]
                doc = csv.DictWriter(csvfile, fieldnames=attribs)
                [doc.writerow(i.to_dictionary()) for i in list_objs]

    @classmethod
    def load_from_file_csv(cls):
        """ serializes and deserializes in CSV """
        csvNew = cls.__name__ + ".csv"
        try:
            with open(csvNew, "r", newline="") as csvfile:
                if cls.__name__ == "Square":
                    attribs = ["id", "size", "x", "y"]
                else:
                    attribs = ["id", "width", "height", "x", "y"]
                doc = csv.DictReader(csvfile, fieldnames=attribs)
                lists = [{k: int(v) for k, v in dic.items()} for dic in doc]
                return [cls.create(**nlist) for nlist in lists]
        except Exception:
            return []
