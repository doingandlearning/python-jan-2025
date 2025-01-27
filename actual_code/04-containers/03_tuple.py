"""
Ordered - Unordered
Mutable - Immutable
Allow duplicates or not
Reference by key or index
Growable or fixed

Tuples
- Ordered
- Immutable
- Allow duplicate members
- Reference by index
- Fixed
"""

empty_tuple = ()
empty_tuple = tuple()

print(empty_tuple)
print(type(empty_tuple))

print(empty_tuple.count("a"))
# print(empty_tuple.index("a"))

tup1 = (1,3,5,7,9)

print(tup1[0])
print(tup1[:3])
print(tup1[1:4])

print(1 in tup1)  # check for membership

# range(10)
for number in tup1:   # loop over/iterate over members
    print(number)

list = ([1,2], 12, True, (True, False))
print(list)