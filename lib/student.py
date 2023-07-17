#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def set_knowledge(self, knowledge):
        self.knowledge = knowledge

    def learn(self, new_string):
        self.knowledge.append(new_string)
        

my_Student = Student('Tim', 'Jones')

print("Has attribute first_name: ", hasattr(my_Student, "first_name"))
print(my_Student.first_name)

print("Has attribute last_name: ", hasattr(my_Student, "last_name"))
print(my_Student.last_name)

print("Has attribute knowledge: ", hasattr(my_Student, "knowledge"))
my_Student.learn("React")
my_Student.learn("Python")
print("knowledge array: ", my_Student.knowledge)

