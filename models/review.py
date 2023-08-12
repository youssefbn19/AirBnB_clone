#!/usr/bin/python3
"""model for class review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """definition of class review that has place_id, user_id, text
    as attr"""
    place_id = ""
    user_id = ""
    text = ""
