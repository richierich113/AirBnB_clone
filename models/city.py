#!/usr/bin/python3
"""creates a User class"""


from models.base_model import BaseModel


class City(BaseModel):
    """ manages city objects"""

    state_id = ""
    name = ""
