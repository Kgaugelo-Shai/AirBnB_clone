#!/usr/bin/python3
""" Represents file storage in JSON"""
import json
import os
#import importlib
import re
import models

class FileStorage:

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
        for k,v in self.__objects.items():
            new_dict[k] = v.to_dict()

        with open(self.__file_path, "w") as j_file:
            json.dump(new_dict, j_file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as j_file:
                obj_data = json.load(j_file)
                for k, v in obj_data.items():
                    class_name = k.split('.')[0]
                    module = __import__('models.base_model',
                                        fromlist=[class_name])
                    instance = getattr(module, class_name)
                    obj = instance(**v)
                    self.new(obj)
