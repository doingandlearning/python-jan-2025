with open("myfile.txt") as file:
    print(file.read())

# Pythonic (Idiomatic Python) to use this kind Context Manager
# - db connections, network connections, files, ...