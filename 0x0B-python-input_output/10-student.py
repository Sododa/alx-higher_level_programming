#!/usr/bin/python3
"""Write a class Student that defines a student by:
    (based on 9-student.py)"""


class Student:
    """
    defines properties of student.
        first_name (str): first name of student.
        last_name (int): last name of student.
    """
    def __init__(self, first_name, last_name, age):
        """ new instances of Student.
            first_name (str): first name of student.
            last_name (int): last name of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.
only attribute names contained in,
        this list must be retrieved.
        Otherwise, all attributes must be retrieved.
            dict: dictionary representation.
        """
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for item in attrs:
            try:
                new_dict[item] = self.__dict__[item]
            except Exception:
                pass
        return new_dict
