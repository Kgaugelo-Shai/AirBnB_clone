#!/usr/bin/python3

import BaseModel
import City
import User
import Amenity

class Place(BaseModel):
    """Represent a place.

    Attributes:
            city_id: The City id.
            user_id: The User id.
            Name: The name of the place.
            description:The description of the place.
    """

    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: 0
    number_bathrooms: 0
    max_guest: 0
    price_by_night: 0
    latitude: 0.0
    longitude: 0.0
    amenity_ids: str = ""
