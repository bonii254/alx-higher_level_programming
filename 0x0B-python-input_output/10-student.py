#!/usr/bin/python3
"""Defines a student class"""


class Student:
    """Represents a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes a student

        Args:
            first_name (str): students first name
            last_name (str): students last name
            age (int): student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """Returns serialization description(dictionary)

            Args:
                obj: an instance of a class
        """
        if (type(attrs) == list and all(type(item) == str for item in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
	return self.__dict__
