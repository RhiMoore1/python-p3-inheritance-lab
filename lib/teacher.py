#!/usr/bin/env python
from user import User
import random

knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]
class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def set_knowledge(self, knowledge):
        if isinstance(knowledge, list) and len(knowledge) > 0:
            self.knowledge = knowledge
   
    def teach(self):
        random_index = random.randint(0, len(knowledge)-1)
        return self.knowledge[random_index]


my_Teacher = Teacher('Tina', 'Smith')

print("Has attribute first_name: ", hasattr(my_Teacher, "first_name"))
print(my_Teacher.first_name)

print("Has attribute last_name: ", hasattr(my_Teacher, "last_name"))
print(my_Teacher.last_name)

print("Has attribute knowledge: ", hasattr(my_Teacher, "knowledge"))
print(my_Teacher.knowledge)

print(my_Teacher.teach())
