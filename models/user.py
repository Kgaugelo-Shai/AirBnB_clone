#!/usr/bin/python3

import BaseModel

class User(BaseModel):

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
