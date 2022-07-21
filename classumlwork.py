from os import sched_get_priority_max
from unicodedata import name


class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print ("hello my name is" + self.name)

p1 = student("John", 36)
p1.myfunc()

p2 = student("Joel", 21)
p2.myfunc()