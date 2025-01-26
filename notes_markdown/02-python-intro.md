# Introduction to the Python World

**Kevin Cunningham**  
Date: 04/08/23

---

## Plan for Session

- Execution Model
- Running Python Programs
- Python IDEs
- Where to get Python
- Common Python Libraries
- Python PIP Environments
- Useful Online Resources

---

## Python Execution Model

- Originated in the 1980s, created by Guido van Rossum
- Not a precompiled language
- Not exactly an interpreted language either

### Simplified Python Execution Process:

1. **Check the Program**: Ensure the program is valid and well-formed.
2. **Compile**: Dynamically compile into the intermediate language.
3. **Run**: Execute the intermediate version of the program.

---

## Running Python Programs

- Commands are stored in a file with a `.py` extension.
- Run the file using the Python command.

---

## Python IDEs

- Several Python IDEs are available:
  - **PyCharm**: Both free and commercial versions.
  - **Visual Studio Code**: Free IDE from Microsoft.
  - **Spyder**: Scientific development applications.
  - **Eclipse + PyDev plugin**: Plugin for Eclipse IDE.
  - **Jupyter Notebooks**: Targeted at data analysis tasks.

---

## Where to Get Python

- Download from [python.org](https://www.python.org/downloads/)

---

## Common Python Libraries

- **Data Science Libraries**

  - NumPy
  - SciPy
  - Pandas
  - Matplotlib

- **Web Frameworks**
  - Django
  - Flask
  - FastAPI
  - Reference: [JetBrains Developer Ecosystem 2022](https://www.jetbrains.com/lp/devecosystem-2022/python/)

---

## Python Environments

- Typically, a tool is used to handle Python environments.
  - Required when working on different projects that use different Python versions (e.g., 3.7, 3.8, 3.9, 3.10) and different libraries.
  - The problem arises because Python installs libraries globally by default.

### Commonly Used Environment Tools:

- **Pip Virtual Environments**: `venv` module
- **Conda Environments**

---

## Pip and Virtual Environments

- Can use virtual environments (`venv` module) to create isolated Python package configurations.
  - Included as part of Python3 and pip.
  - Use `source` to activate on Mac (or `activate.bat` on Windows).

### Example:

```bash
$ python -m venv venv3
$ source venv3/bin/activate
(venv3) $ pip install <package-name>
```

- Install packages from [Python Package Index](https://pypi.org/).

---

## Working with Pip

- **Check Installation**: `pip --version`
- **Install Package**: `pip install <package-name>`
- **Create a Virtual Environment**: `python -m venv venvProj1`
- **Activate Environment**: `source venvProj1/bin/activate`
- **Deactivate Environment**: `deactivate`
- **Update pip**: `pip install --upgrade pip`
- **View Installed Packages**: `pip freeze`

### Example of Using Pip:

```bash
% mkdir bbclabs
% cd bbclabs
% python -m venv venv3
% source venv3/bin/activate
(venv3) % pip --version
pip 22.3.1 from ../bbclabs/venv3/lib/python3.11/site-packages/pip (python 3.11)
(venv3) % pip install pandas
```

- Output shows successful installation of packages like pandas, numpy, etc.

---

## Useful Resources

- **Python Software Foundation**: [Wikipedia](https://en.wikipedia.org/wiki/Python_Software_Foundation)
- **Main Python 3 Documentation Site**: [docs.python.org](https://docs.python.org/3/)
- **List of Built-in Features**: [Python Standard Library](https://docs.python.org/3/library/index.html)
- **Python Module of the Week**: [pymotw.com](https://pymotw.com/3)
- **Python Resources for Beginners**: [Beginners Guide](https://wiki.python.org/moin/BeginnersGuide/Programmers)
- **W3Schools Intro to Python**: [W3Schools](https://www.w3schools.com/python/)

---

## Questions?

?
