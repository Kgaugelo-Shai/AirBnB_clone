#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime, date , time
import models
from models.engine.file_storage import FileStorage

class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Intializing a new BaseModel

        Attributes:
            id (str): unique id string given to each object
            created_at: datetime object with time of creation,
                        format "%Y-%m-%dT%H:%M:%S.%f"
            updated_at: datetime object with time object was updated
                        format "%Y-%m-%dT%H:%M:%S.%f"
        """

        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k in ["created_at", "updated_at"]:
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, v)
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Returns [<class name>] (<self.id>) <self.__dict__>"""
        classname = self.__class__.__name__
        return ("[{}] ({}) {}".format(classname, self.id, self.__dict__))

    def save(self):
        """ updates the updated_at to the current times. """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values"""
        data_dict = self.__dict__.copy()
        data_dict['__class__'] = self.__class__.__name__
        data_dict['created_at'] = self.created_at.isoformat()
        data_dict['updated_at'] = self.updated_at.isoformat()
        return data_dict

    #update __init__(self, *args, **kwargs)
    # if kwargs is not empty:
    # each key of this dictionary is an attribute name
    # each value of this dictionary is the value of this attribute name
    # created_at and updated_at are strings in this dictionary,
    # but inside your BaseModel instance is working with datetime object.
    # You have to convert these strings into datetime object.
    # Tip: you know the string format of these datetime
    # create id and created_at as you did previously (new instance)
