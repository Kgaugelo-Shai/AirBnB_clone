#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime, date , time

class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self):
        """Intializing a new BaseModel"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at
    
    def __str__(self):
        """Returns [<class name>] (<self.id>) <self.__dict__>"""

        classname = self.__class__.__name__
        return ("[{}] ({}) {}".format(classname, self.id, self.__dict__)
    
    def save(self):
        """Updates the updated_at with the current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values"""
        data_dict = self.__dict__.copy()
        data_dict['__class__'] = self.__class__.__name__
        data_dict['created_at'] = self.created_at
        data_dict['updated_at'] = self.updated_at
