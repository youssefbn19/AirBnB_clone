#!/usr/bin/python3
"""model for class city"""
from models.base_model import BaseModel


class City(BaseModel):
    """definition of class city
    with 2 attrs: name and state_id"""
    state_id = ""
    name = ""
