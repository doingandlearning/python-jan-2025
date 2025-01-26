# Lab 10: Modules

The aim of this lab is to modify the existing application so that it makes use of multiple modules rather than being defined in a single file.

Break your application up into two or more modules as you consider appropriate. For example, you might have:

- **readings module**: To hold the `Reading`, `TemperatureReading`, and `RainfallReading` classes.
- **utils module**: For utility functions such as `celsius_to_fahrenheit`, `average`, `minimum`, etc.
- **main module**: For the main application code.

Make sure you import from the modules as appropriate into other modules. For example, in the main application file (for example, `main.py` or `app.py`), you would need to import:

```python
from readings import TemperatureReading
from readings import RainfallReading
from utils import *
```

Now that we know about modules and the main module, you should modify your main application module to check that it is being run as the main module before starting the application.

To do this, you should define a `main` function for your application code.

Then add a test to verify the module is being run as the main module, for example:

```python
if __name__ == "__main__":
    main()
```

```