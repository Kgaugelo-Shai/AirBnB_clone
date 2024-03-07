#!/usr/bin/python3
""" Represents file storage in JSON"""
import json
import os

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
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists
        """
        # check if file exists, if does not pass
        # otherwise, we deserialize
        # open file, read file
        # loop through the whole file
        # find key value pair in the file
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as j_file:
                json_dict = json.loads(j_file)
                self.deserialize_obj(json_dict)

    def deserialize_obj(self, obj):
        """ Deserializes JSON data into objects """
        for k, v in json_dict.items():
            class_name = key.split(".")[0]
            obj_class = globals().get(class_name)
            if obj_class is not None:
                obj = obj_class(**v)
                json_dict[k] = obj
            else:
                print(f"Class {class_name} not found.")
