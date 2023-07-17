#!/usr/bin/env python

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


my_User = User('my', 'user')
# print(my_User.first_name)
# print(my_User.last_name)
# print(hasattr(my_User, "first_name"))
# print(hasattr(my_User, "last_name"))