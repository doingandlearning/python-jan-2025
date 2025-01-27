print("Welcome to this amazing program")
user_name = input("What is your name? ")  # stop ... blocking operation alert()

print("Hello, " + user_name + ", how are you?")  # concatenated strings!

print(f"Hello, { user_name }, how are you?")
print(f"1 + 1 = { 1 + 1 }")

first_number = int(input("What is your first number? "))  # string!  int/float
second_number = input("What is your second number?")

print(f"{first_number} + {second_number} = {first_number + float(second_number)}")

print(str(first_number) + " + " + str(second_number) + " = " + str(first_number + float(second_number)))
