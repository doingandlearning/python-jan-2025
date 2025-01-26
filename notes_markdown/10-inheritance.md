# Plan for Session
- What is Inheritance?
- Inheritance Terminology
- Purpose of a Subclass
- Declaring Inheritance in Python
- The Class object and Inheritance
- Overriding and Extending Methods
- Inheritance Naming Conventions
- Multiple Inheritance

---

## What is Inheritance?
- Allows one class to inherit features defined in another class.
- Provides a form of reuse.
- Allows data and behavior to be defined in one place and therefore maintained in one place.

### Example:
- Class `Person` defines `name`, `age` attributes and `birthday()` method.
- Class `Employee`:
  - Inherits the definitions of `name`, `age`, and `birthday()`.
  - Adds `id` attribute and `calculate_pay()` method.

---

## Inheritance Terminology
- **Superclass**: The class being inherited from.
- **Subclass**: The class that inherits from the superclass.
- **Instance**: An object created from a class, which may be from either a superclass or subclass.

---

## Purpose of a Subclass
- A subclass should do one or more of the following:
  - **Extend** the external protocol or interface of the superclass.
  - **Change** the implementation of one or more methods, i.e., the way in which the behavior provided by the superclass is implemented.
  - **Add** additional behavior that references inherited behavior/data.

---

## Declaring Inheritance
- A class extends a parent class by listing the parent in brackets after the class name.

### Example:
```python
class SubClassName(SuperClassName):
    class-body
```
- A subclass will inherit all attributes and methods from the superclass unless they override them.

### Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        print('Happy birthday! You were', self.age)
        self.age += 1
        print('You are now', self.age)

class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id

    def calculate_pay(self, hours_worked):
        rate_of_pay = 7.50
        if self.age >= 21:
            rate_of_pay += 2.50
        return hours_worked * rate_of_pay
```

- **Employee extends Person**:
  - The `__init__()` method must reference the `__init__()` method in class `Person`, used to initialize instances of that class via the `super().__init__()` reference.
  - All instances of the class `Employee` have a `name`, `age`, and an `id` and have the behaviors `birthday()` and `calculate_pay(hours_worked)`.
  - `calculate_pay()` in the `Employee` class can access attributes `name` and `age` just as it can access `id`.

---

## Inheritance Usage Example
### Example:
```python
print('Person')
p = Person('John', 54)
print(p)
p.birthday()
print(p.name)
print(p.age)

print('-' * 25)
print('Employee')
e = Employee('Denise', 51, 7468)
print(e)
e.birthday()
print(e.name)
print(e.age)
print(e.id)
print('e.calculate_pay(40):', e.calculate_pay(40))
```
- Output:
  - Person: John is 54, Happy birthday you were 54, You are now 55, John, 55.
  - Employee: Denise is 51 - id(7468), Happy birthday you were 51, You are now 52, Denise, 52, 7468, `e.calculate_pay(40)`: 400.0.

---

## The Class object and Inheritance
- Every class extends one or more classes, even the class `Person`.
- By default, it extends the class `object`.

### Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
```
- These two are equivalent.

---

## The Class `object` Behavior
- The `object` class provides some default special methods.
- Defines special methods such as `__str__()`, `__init__()`, `__eq__()` (equals), and `__hash__()` (hash method).

### Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ' is ' + str(self.age)

class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id

    def __str__(self):
        return self.name + ' is ' + str(self.age) + ' - id(' + str(self.id) + ')'
```

---

## Overriding Methods
- Occurs when a subclass defines a method with the same signature as a parent class.
- The method in the subclass overrides the method in the parent class.

### Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ' is ' + str(self.age)

class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id

    def __str__(self):
        return super().__str__() + ' - id(' + str(self.id) + ')'
```

---

## Extending Methods
- May want to extend behavior in a parent class.
- Achieved via a call to the `super()` version of the method.

### Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ' is ' + str(self.age)

class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id

    def __str__(self):
        return super().__str__() + ' - id(' + str(self.id) + ')'
```

---

## Inheritance Naming Conventions
- **Single underbar convention**:
  - Methods or attributes to be considered protected, private to the class but can be accessed from any subclass.
  - Scope is thus the class and any subclasses (but this is only a convention).

- **Double underbar convention**:
  - Methods or attributes to be considered private to that class.
  - Should not be called from outside of the class.
  - Python runtime can perform name mangling on these.

---

## Python Multiple Inheritance
- Python supports multiple inheritance.
- Multiple superclasses are listed in the parent class list (defined by the brackets following the class name).

### Example:
```python
class Car:
    """ Car """

    def method1(self):
        pass

class Toy:
    """ Toy """

    def method1(self):
        pass

class ToyCar(Car, Toy):
    """ A Toy Car """
```
- To find methods, Python 3 performs a breadth-first search up the inheritance tree.

---

## Questions?

?
