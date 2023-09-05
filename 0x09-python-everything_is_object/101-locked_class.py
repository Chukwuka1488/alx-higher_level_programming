#!/usr/bin/python3
class LockedClass:
    """A locked class that only allows creating an instance attribute 'first_name'"""

    __slots__ = ['first_name']
