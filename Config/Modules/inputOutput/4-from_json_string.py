#!/usr/bin/python3

"""
A function that returns an object (Python data structure) represented
by a JSON string
"""

import json


def from_json_string(my_str):
    """
    From JSON string to Object
    """

    return json.loads(my_str)
