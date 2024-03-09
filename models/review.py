#!/usr/bin/python3

import BaseModel
import Place
import User

class Review(BaseModel):
    """Represents a user's review.
    
    Attributes:
            place_id: The Place's id.
            user_id: The User's id.
            text: The review text.
    """

    place_id: str = ""
    user_id: str = ""
    text: str = ""
