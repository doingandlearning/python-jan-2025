"""
Defining Functions
Zero, single and multiple parameter options
Default Parameter Values
Named Parameters
Returning Values
Returning Multiple Values
Arbitrary Parameter Lists
"""

## No parameters, no return value


def print_message():
    """
    This will always print the same message and should be used ...
    """
    print("This is a message")



print_message()

def print_message(message, number_of_dashes = 25, is_shouting = False):  # parameters
    """
    This prints a message and finishes with dashes.
    :param message: A unique message for your messages
    """
    if is_shouting:
        print("HEAR YE, HEAR YE!!!")
        print(str(message).upper())
    else:
        print("Hear ye, hear ye!")
        print(message)
    print("-" * number_of_dashes)


# positional argument
# named/keyword argument

print_message(is_shouting=True, message="This is a message I would like to shout")  # arguments
print_message("Functions are cool!", 50, True)


