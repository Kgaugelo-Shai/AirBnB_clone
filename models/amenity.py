#!/usr/bin/python3
""" Represents an Amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ The Amenities class

        Attributes:
           name (str): a string holding name
    """

    name: str = ""
