#!/usr/bin/env python3
"""Module that pickles and unpickles a custom Python object."""
import pickle


class CustomObject:
    """A simple object holding a name, an age and a student status."""

    def __init__(self, name, age, is_student):
        """Initialize the object's attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes, one per line."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Pickle this instance into filename; return None on failure."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Unpickle and return an instance from filename, or None."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
