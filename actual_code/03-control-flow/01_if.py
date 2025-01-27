# num = int(input("Enter a number: "))
#
# if num < 0:   # < <= > >= ==
#     # do something in here
#      print(f"{num} is a negative number")
#      print("this is not spaced properly")
# else:
#     if num > 10:
#         print(f"{num} is a positive number that is greater than 10.")
#     print(f"{num} is a positive number")

print("If block is over!")

# savings = float(input("Enter how much do you have in savings? "))
#
# if savings == 0:
#     print("Sorry no savings!")
# elif savings < 500:
#     print("Well done!")
# elif savings < 1000:
#     print("That is a tidy sum!")
# else:
#     print("Well done for saving!")
#

snowing = False
temp = -1

if temp < 0:
    print("It is freezing!")
    if snowing:
        print("Put on boots")
    print("Time for hot chocolate")
print("Goodbye")

if temp < 0 or snowing:  # and or not
    print("Put on boots")

if not snowing:
    print("is it raining then?")

if None:
    print("Will this print?")  # y/n ?

    # Falsey values: None, "", 0, []
    # ALmost everything else is True!