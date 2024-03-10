#!/usr/bin/python3
""" Represents a Review Class """
from models.base_model import BaseModel


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
