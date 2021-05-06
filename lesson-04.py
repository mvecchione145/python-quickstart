# --STEP LIST--
# 1. Check out lessonfour/utilities.py
#     Observe the lessonfour/__init__.py file this is needed to tell python lessonfour is a package.

# 2. Run this script.
#     In your command line terminal window execute the following line:
#     python lesson-04.py

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


from lessonfour.utilities import simple_double_function, MyObject


b = simple_double_function(3)
obj = MyObject("Bob Segert", 2)

c = obj.simple_multiplier(4)
print("-- results --")
print(b)
print("")
print(c)
