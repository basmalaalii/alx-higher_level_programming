#!/usr/bin/python3
'''task 10 module'''


class Student:
    '''student class'''
    def __init__(self, first_name, last_name, age):
        '''Initializes the student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''returns a dictionary representation of a Student instance
        If attrs is a list of strings, only attributes names contained
        in this list must be retrieved.
        otherwise, all attributes must be retrieved
        '''
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return seld.__dict__
        except Exception:
            return seld.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict
