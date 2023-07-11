#!/usr/bin/python3
"""
class student with defined attributes
"""


class Student:
    """
    defines the attributes
    """
  
    def __init__(self, first_name, last_name, age):
        """
        instantiation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns dictionary rep of all instances
        """
        return (self.__dict__)
