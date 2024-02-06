#!/usr/bin/python3
"""Write a class Student that defines a student by:"""


class Student:
    """
    Class that defines properties of student.

    Attributes:
        first_name (str): first name of student.
        last_name (int): last name of student.
    """
    def __init__(self, first_name, last_name, age):
        """Creates new instances of Student.
            first_name (str): first name of student.
            last_name (int): last name of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
