list1 = [1,2,3,4]
list2 = list1.copy()

list2.append(5)

print(list1)
print(list2)

# what happens if you replace a value that is duplicated in a list
# - does it replace all occurrences of that value?

list1 = ["George", "Sam", "Dan", "George"]

print(list1.index("George"))
list1[0] = "Dan"
print(list1)

print("George george George George".replace("George", "Dan"))