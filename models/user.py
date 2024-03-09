#!/usr/bin/python3

import BaseModel

class User(BaseModel):
    """ Represent a user.
    Attributes:
            email: The user's email.
            password: The user's password.
            first_name: The user's first name.
            last_name: The user's last name.
    """

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
