# --STEP LIST--
# 1. Run this script.
#     In your command line terminal window execute the following line:
#     python lesson-03b.py

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

# The results should look like this:
# -- object --
# <__main__.MyObject object at {some random identifier}>
#
# -- name --
# Jonathan Bush
#
# -- multiplier --
# 3
#
# -- result --
# 12


class MyObject:
    def __init__(self, name, multiplier):
        self.name = name
        self.multiplier = multiplier

    def simple_multiplier(self, a):
        return a * self.multiplier


obj = MyObject("Jonathan Bush", 3)
print("-- object --")
print(obj)
print("")
print("-- name --")
print(obj.name)
print("")
print("-- multiplier --")
print(obj.multiplier)
print("")

b = obj.simple_multiplier(4)
print("-- result --")
print(b)
