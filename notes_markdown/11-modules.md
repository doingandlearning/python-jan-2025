# Plan for Session
- Python Modules
- Importing Modules
- Using `from` with `import`
- Main Module
- Importing non-local modules
- Module Search Path

---

## Python Modules
- A Python module is a file with:
  - Variables and Functions
  - Classes and objects
  - Executable code
  - Attributes associated with the module such as its name
  - Module docstring (optional)

- The name of a module is the name of the file (minus the suffix `.py`).
  - e.g., `utils.py` defines the module `utils`.

---

## Example `utils` Module
- Contains a function `printer` and a class `Shape`.

### Example:
```python
"""This is a test module"""
print('Hello, I am the utils module')

def printer(some_object):
    print('printer')
    print(some_object)
    print('done')

class Shape:
    def __init__(self, id):
        self.id = id
        
    def __str__(self):
        return 'Shape - ' + self.id

default_shape = Shape('square')
```
- The module has a comment at the start of the file—useful documentation for anyone working with the module.
- The module also has some executable code (the `print` statement just after the comment) that will be run when the module is loaded/initialized by Python.
- A variable `default_shape` is also initialized when the module is loaded and can be referenced outside the module.

---

## Importing a Module
- Most modules are not automatically imported; you must explicitly import them using the `import` statement.
- Use the name of the module (not the file).

### Example:
```python
import utils

utils.printer(utils.default_shape)
shape = utils.Shape('circle')
utils.printer(shape)
```

- What happens when we run the code:
  - The free-standing code executed when the module was first imported, i.e., ran `print('Hello, I am the utils module')` and initialized the `default_shape`.
  - Then the application code ran.

---

## Importing Multiple Modules
- There can be any number of modules imported—both user-defined modules and system-provided modules.
- Modules can be imported via separate `import` statements or by supplying a comma-separated list of modules.

### Example:
```python
import utils
import support
import module1, module2, module3
```
- Common convention is to place all `import` statements at the start of a file; however, this is only a convention and `import` statements can be placed anywhere in a file prior to where the module’s features are required.

---

## Importing from a Module
- Previous examples still required the name of the module.
- Can avoid this using `from <module name> import *`.
- Can now reference module contents directly.
- Or can import only those elements of interest.
- Can provide aliases.

### Example:
```python
from utils import *

printer(default_shape)
shape = Shape('circle')
printer(shape)

from utils import Shape

s = Shape('rectangle')
print(s)

from utils import printer as myfunc
import utils as utilities

utilities.printer(utilities.default_shape)
```
- Note: Wildcard import will import everything unless an element starts with an underbar (`_`), in which case it must be imported explicitly.

---

## Main Module
- When a module is loaded, any free-standing code will execute.
- May only want this to happen if the module is the entry point to the program.
- When the module is the entry point, then it has a special name `__main__`.
- Can test for this and only run code if the module is being run as the main module—a common idiom in Python programs.

### Example:
```python
if __name__ == "__main__":
    print('Only run if main module')
```

- Common to define a function called `main()` invoked when run as the main module.

### Example:
```python
from utils import *

def main():
    printer(default_shape)
    shape = Shape("circle")
    printer(shape)

if __name__ == "__main__":
    main()
```

---

## Importing non-local Modules
- Built-in or third-party modules can be imported via their name.
- The `sys` module is a built-in module that provides information about the system.

### Example:
```python
import sys

print('sys.version:', sys.version)
print('sys.maxsize:', sys.maxsize)
print('sys.path:', sys.path)
print('sys.platform:', sys.platform)
```

---

## Python Module Search Path
- Python will search for libraries in the current directory.
- Note: Can therefore hide a module/library.
- Directories listed in `sys.path`.
- The `sys.path` is set up when Python starts up and may reference a virtual environment.

---

## Questions?

?
