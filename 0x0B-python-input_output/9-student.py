#!/usr/bin/python3
"""Contains the clas "Student"""

class student:
    """Representation of a student"""
    def init (self, first name, last name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to json (self):
        """returns a dictionary representation of a Student instance"""
        return self.__dict__
