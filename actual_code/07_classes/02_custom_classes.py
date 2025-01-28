# Classes should be named in CamelCase - like ThisIsAClassName

class Person:
    """
    A Person class
    :field: age
    :field: name

    :method: calculate_pay
    :method: birthday
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"I have been initialised: {self}")

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

    def __str__(self):
        return f"{self.name}, {self.age} years old."

    def birthday(self):
        print(f"Happy Birthday {self.name}! You were {self.age}")
        self.age += 1
        print(f"You are now, {self.age}")

    def calculate_pay(self, hours_worked):
        rate_of_pay = 10
        if self.age >= 21:
            rate_of_pay += 2.5
        return hours_worked * rate_of_pay

    def is_teenager(self):
        return 20 > self.age > 12


person = Person("Dan", 91)
person2 = Person("Ethan", 12)

# Protocols ...
print(person)  ## __repr__ __str__  - Person(name, age)
print(person2) ## Ethan is 12  - Person(name, age)
# new_person = person
# print(id(new_person))

print(person2.name)
print(person2.age)

print([person, person2])

print(repr(person))

person.birthday()
person2.birthday()

print(person.calculate_pay(5))
print(person2.calculate_pay(5))

print(person.is_teenager())
print(person2.is_teenager())

del person2
print(person2)