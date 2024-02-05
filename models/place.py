#!/usr/bin/python3
"""
Module for Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherits from BaseModel

    Public Class Attributes:
        city_id (str) : City.id
        user_id (str) : User.id
        name (str) : name of place
        description (str) : description of place
        number_rooms (int) : the number of rooms in place
        number_bathrooms (int) : the numbe of bathrooms in place
        max_guest (int) : the maximum number of guests in place
        price_by_night (int) : the nightly price of place
        latitude (float) : the latitude of place
        longitude (float) : the longitude of place
        amenity_ids (list) : a list of Amenity.ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
