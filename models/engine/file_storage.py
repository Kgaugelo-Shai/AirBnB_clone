#!/usr/bin/python3
""" Represents file storage in JSON"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ Represents FileStorage Class

    Attributes:
        __file_path (str): A string representation of path to JSON file.
        __objects (dict): A dictionary containing instantiated objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects. """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name.id>."""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ serialize __objects to the JSON file (path:__file_oath)"""
        # created an empty dictionary
        # loop throught __object dictionary with k, v pairs
        # new_dict[key] = obj.to_dict
        # opened a file
        # dumped the new_dict to file
        new_dict = {}
        for k, v in FileStorage.__objects.items():
            new_dict[k] = v.to_dict()

        with open(FileStorage.__file_path, "w") as j_file:
            json.dump(new_dict, j_file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if (os.path.exists(FileStorage.__file_path)
                and os.path.getsize(self.__file_path) > 0):
            with open(FileStorage.__file_path, 'r') as j_file:
                obj_data = json.load(j_file)
                for value in obj_data.values():
                    class_name = value["__class__"]
                    del value["__class__"]
                    obj = eval(class_name)(**value)
                    self.new(obj)
