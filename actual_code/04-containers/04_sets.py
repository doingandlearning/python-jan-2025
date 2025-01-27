"""
Ordered - Unordered
Mutable - Immutable
Allow duplicates or not
Reference by key or index
Growable or fixed

Sets
- Unordered
- Mutable
- Disallow duplicate members
- Don't know what order - can't! Reference by index
- Growable
"""

empty_set = set()
print(empty_set)
print(type(empty_set))

set1 = {"orange", "pineapple", "blackcurrant", "orange"}

print(set1)

print("orange" in set1)
print("blueberry" in set1)

set1.add("blueberry")
set1.add("orange")
set1.add("blackcurrant")

print(set1)

licence_holders = {"John", "Dan", "Darren", "Jui"}
live_in_london = {"Dan", "Leoni", "Jui"}

print(licence_holders.intersection(live_in_london))
print(licence_holders.symmetric_difference(live_in_london))

set1 = list(set(["orange", "pineapple", "blackcurrant", "orange"]))
print(set1)