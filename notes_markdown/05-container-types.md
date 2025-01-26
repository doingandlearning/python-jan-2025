# Plan for Session
- Characteristics of Data Containers
- Python Collection Types
- Tuples
- Lists
- Dictionaries
- Collection constructor functions
- Check for membership & iterations

---

## Characteristics of Data Containers
- Allow multiple values to be held together
- Have a set of features:
  - Ordered or unordered
  - Mutable or immutable (modifiable or not)
  - Allow duplicates or not
  - May associate a value with an index or key
  - May be growable or not
- Choose appropriate container type based on your requirements
- Often referred to as collections

---

## Python Collection Types
### Tuples:
- Represent a collection of values
  - Ordered
  - Fixed size
  - Immutable (cannot be modified)
  - Allow duplicate members
  - Indexed

### Lists:
- Ordered
- Mutable (changeable)
- Allow duplicate members
- Indexed
- Growable

### Sets:
- Unordered
- Growable
- Mutable (changeable)
- Do not allow duplicate values
- Can only hold immutable objects

### Dictionaries:
- Ordered (3.7 onwards; unordered prior to 3.7)
- Mutable (changeable)
- Indexed by a key which references a value
- Growable

---

## Tuples
- Immutable ordered collections

### Example:
```python
empty_tuple = ()
tup1 = (1, 3, 5, 7)
print('tup1[0]:\t', tup1[0])
print('tup1[1]:\t', tup1[1])
print('tup1[1:3]:\t', tup1[1:3])  # return a slice
print('tup1[:3]:\t', tup1[:3])
print('tup1[1:]:\t', tup1[1:])
print('len(tup1):\t', len(tup1))

tup2 = (1, 'John', True, -23.45)
print(tup2)

tup3 = ('apple', 'pear', 'orange', 'plum', 'apple')
for fruit in tup3:
    print(fruit)

if 'orange' in tup3:
    print('orange is in the Tuple')
```

---

## Nested Tuples
- Can nest tuples

### Example:
```python
tuple1 = (1, 3, 5, 7)
tuple2 = ('John', 'Denise', 'Phoebe', 'Adam')
tuple3 = (42, tuple1, tuple2, 5.5)
print(tuple3)
print(tuple3[1][1])
```

---

## Lists
- Mutable ordered container

### Example:
```python
empty_list = []  # empty_list = list()
list1 = ['John', 'Paul', 'George', 'Ringo']
print(list1, ':', len(list1))
print('list1[1]:', list1[1])
print('list1[1:3]:', list1[1:3])  # obtain a slice from 1 up to 3
print('list[:3]:', list1[:3])     # obtain a slice from start up to 3
print('list[1:]:', list1[1:])     # obtain a slice from start 1 to end

list1.append('Pete')
print(list1)
list1.extend(['Albert', 'Bob'])
print(list1)

list1.insert(2, 7)
print(list1)

list1.remove('Pete')
print(list1)

del list1[1:3]
print(list1)
```

---

## List Methods
| Method | Description |
| --- | --- |
| `append()` | Adds an element at the end of the list |
| `clear()` | Removes all the elements from the list |
| `copy()` | Returns a copy of the list |
| `count()` | Returns the number of elements with the specified value |
| `extend()` | Add the elements of a list (or any iterable) to the end of the current list |
| `index()` | Returns the index of the first element with the specified value |
| `insert()` | Adds an element at the specified position |
| `pop()` | Removes the element at the specified position |
| `remove()` | Removes the item with the specified value |
| `reverse()` | Reverses the order of the list |
| `sort()` | Sorts the current list |

---

## Nested Lists
- Can nest lists

### Example:
```python
l1 = [1, 43.5, 'Phoebe', True]
l2 = ['apple', 'orange', 31]
root_list = ['John', l1, l2, 'Denise']
print(root_list)
print(root_list[1][1])
```

---

## Nesting Tuples and Lists
- Can nest tuples and lists

### Example:
```python
t1 = (1, 'John', 34.5)
l1 = ['Smith', 'Jones']
l2 = [t1, l1]
t2 = (l2, 'apple')
print(t2)
```

---

## Dictionaries
### Set of key:value pairs

### Example:
```python
empty_dictionary = {}

cities = {
    'Wales': 'Cardiff',
    'England': 'London',
    'Scotland': 'Edinburgh',
    'Ireland': 'Dublin'
}
print(cities)
```

---

## Working with Dictionaries
### Example:
```python
print('cities[Wales]:', cities['Wales'])
print('cities.get(Ireland):', cities.get('Ireland'))

for country in cities:
    print(country, end=' ')
    print(cities[country])

print(cities.values())
print(cities.keys())
print(cities.items())
print('Wales' in cities)
print('France' not in cities)

del cities['Scotland']  # Delete
cities['France'] = 'Paris'  # Add
cities['Wales'] = 'Swansea'  # Replace
```

---

## Nesting Dictionaries
- Keys must be immutable, but values can be any type of object, including collections.

### Example:
```python
seasons = {
    'Spring': ('Mar', 'Apr', 'May'),
    'Summer': ('June', 'July', 'August'),
    'Autumn': ('September', 'October', 'November'),
    'Winter': ('December', 'January', 'February')
}
print(seasons['Spring'])
print(seasons['Spring'][1])
```

---

## Dictionary Methods
| Method | Description |
| --- | --- |
| `clear()` | Removes all the elements from the dictionary |
| `copy()` | Returns a copy of the dictionary |
| `fromkeys()` | Returns a dictionary with the specified keys and values |
| `get()` | Returns the value of the specified key |
| `items()` | Returns a list containing the tuple for each key-value pair |
| `keys()` | Returns a list containing the dictionary's keys |
| `setdefault()` | Returns the value of the specified key. If the key does not exist: insert the key with the specified value |
| `update()` | Updates the dictionary with the specified key-value pairs |
| `values()` | Returns a list of all the values in the dictionary |

---

## Collection Constructor Functions
- Take an iterable (anything implementing the iterable protocol, e.g., lists, tuples, sets, etc.)
- Return a type of collection

### Example:
```python
tuple(iterable)
list(iterable)
set(iterable)

dict2 = dict([('uk', 'London'), ('ireland', 'Dublin'), ('france', 'Paris')])
```

---

## Check for Membership of Containers
- Can check to see if a value is in a container
- Use the `in` and `not in` operators
- Can be used with tuples, lists, sets, dictionary keys, etc.

### Example:
```python
# Tuples
fruit = ('apple', 'pear', 'orange', 'plum', 'apple')
if 'orange' in fruit:
    print('orange is in the Tuple')
if 'orange' not in fruit:
    print('orange is NOT in the Tuple')

# Lists
list1 = ['John', 'Paul', 'George', 'Ringo']
if 'Pete' in list1:
    print('Pete in the list')
else:
    print('Pete not in the list')

# Dictionaries
cities = {
    'Wales': 'Cardiff',
    'England': 'London',
    'Northern Ireland': 'Belfast',
    'Ireland': 'Dublin'
}
if 'Wales' in cities:
    print('We know the capital of Wales')
```

---

## Iterating Through Containers
- Can iterate through all the values in a container such as a list, a tuple, or a set.
- Use a `for` loop.

### Example:
```python
# Set up the list
list = [1, 3, 5, 7, 9]

# Using for loop
for i in list:
    print(i)
```

- With a dictionary, can iterate over the keys or values.

### Example:
```python
# Note keys are not strings
dict1 = dict(uk='London', ireland='Dublin', france='Paris')

# Iterate over the keys
for key in dict1:
    print(key)

# Iterate over the values (items) in the dictionary
for value in dict1.values():
    print(value)
```


## Questions?

?
