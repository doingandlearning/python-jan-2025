"""
Ordered - Unordered
Mutable - Immutable
Allow duplicates or not
Reference by key or index
Growable or fixed

Lists
- Ordered
- Mutable
- Allow duplicate members
- Reference by index
- Growable
"""

empty_list = []
print(type(empty_list))
empty_list = list()

beatles = ["George", "Paul", "John", "Ringo"]
print(beatles)
print(len(beatles))
print(beatles[3])   # who is at position 3?
print(beatles[0:2])    # everyone from position 0 up to but not including position 2
print(beatles[:3])  # everyone from the start up to but not including position 3.
print(beatles[1:])

beatles.append("Leoni")  # add a single element
print(beatles)

beatles.extend(["Dan", "Darren", "Jui"])  # add another "iterable" of elements
print(beatles)

beatles.insert(3, "Mahgoub")
print(beatles)

beatles.append(True)
beatles.append([1,2,3])
print(beatles)

print(beatles.pop())
print(beatles)

list_of_lists = [["Mahgoub", "Luke", "George"], ["Dan", "Darren", "Leoni"]]
print(list_of_lists[0][1])




"""
append()
Adds an element at the end of the list
clear()
Removes all the elements from the list
copy()
Returns a copy of the list
count()
Returns the number of elements with the specified value
extend()
Add the elements of a list (or any iterable), to the end of the current list
index()
Returns the index of the first element with the specified value
insert()
Adds an element at the specified position
pop()
Removes the element at the specified position
remove()
Removes the item with the specified value
reverse()
Reverses the order of the list
sort()
Sorts the current list

"""

beatles = ["George", "Paul", "John", "Ringo"]
beatles[0] = "Bob"
print(", ".join(beatles))