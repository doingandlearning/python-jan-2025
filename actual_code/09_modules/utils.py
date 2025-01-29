"""
This is a module of utility functions.
"""



def printer(some_object):
    print('printer')
    print(some_object)
    print('DONE')

class Shape:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f"Shape[{self.type}]"

default_shape = Shape("triangle")


if __name__ == "__main__":
    print("Hello I am the utils module")
    print("This is utils.py: " + __name__)