valid_data = False

while not valid_data:
    age = int(input("Please enter your age: "))
    if age < 0 or age > 120:
        print("Invalid age")
    else:
        valid_data = True

print(f"Hello, what's it like being {age} years old?")

while True:
    print("Python rocks 🐍")
    break

while True:
    print("Python rocks 🐍")
    continue
    print("I will never print")

# invalid_data = True

# while invalid_data: