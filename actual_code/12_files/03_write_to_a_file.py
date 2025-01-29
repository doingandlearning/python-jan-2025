import traceback
try:
    with open("myfile.txt", mode="w") as file:
        file.write("Hello\n")
        file.write("How are you?\n")
        file.writelines(["I'm fine thanks\n", "What do you think of files?\n", "They're okay\n"])

except Exception as exp:
    print(exp)
    traceback.print_exc()