#!/usr/bin/python3

import BaseModel
import Place
import User

class Review(BaseModel):

    place_id: str = ""
    user_id: str = ""
    text: str = ""
