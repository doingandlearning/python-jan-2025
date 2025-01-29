file = open("myfile.txt", mode="r")  # file handle!

print(file.read().split("\n"))  # returns a string version of the whole file
file.seek(0)
print(file.readlines())  # returns a list of lines (new line characters are still there)
file.seek(0)
print(file.readline())  # lazy evaluating line by line
file.seek(0)

line = file.readline()  # loads a single line

while line:
    if line.find("Me") > -1:
        print(line)
    line = file.readline()

file.seek(0)

for line in file.readlines(): # loads the entire file into memory
    if line.find("Me") > -1:
        print(line)





file.close()

