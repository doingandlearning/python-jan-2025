data = [1, 3, 5, 2, 7, 4, 1.5, 6]

# I want all the even numbers
def is_even(val):
    return val % 2 == 0

result = []

for num in data:
    if is_even(num):
        result.append(num)

print(result)


# Higher Order Function - a function that takes another function as an argument and/or
# returns a function as a result
print(list(filter(lambda num: num % 3 == 0, data)))  # pandas
print([num for num in data if num % 3 == 0])  # list comprehension



print(list(map(lambda num: num * 3, data)))   # data is unchanged!
print([user * 3 for user in data])
# List Comprehension

people = [
    {"name": "Jui", "age": 21},
    {"name": "Dan", "age": 91},
    {"name": "Luke", "age": 42}
    ]

print(people)

def person_age(person):
    return person["age"]

print(sorted(people, key=lambda person: person["name"]))
