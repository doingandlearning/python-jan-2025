from utils import Shape as UtilsShape
import utils as u
from datetime import datetime as dt
from utils import *
import sys
import numpy as np

numpyList = np.array([1,2,3,4])
print(numpyList)


def main():
    print(u)
    circle = UtilsShape("circle")
    print(circle)
    print(u.default_shape)
    print("This is app.py:" + __name__)
    print(sys.version)
    print(sys.maxsize)
    print(sys.path)
    print(sys.platform)
    print(dt.now())


if __name__ == "__main__":
    main()