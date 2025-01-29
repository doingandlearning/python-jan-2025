import traceback

def divide(a,b):
    return a / b


# result = divide(4/5)
try:
    result = divide(4/5)
    print(result)
    raise SyntaxError("You did it wrong - duh!")
except ZeroDivisionError as exp:
    print("Oh! It looks like you tried to divide by 0. You can't do that!")
    # ping the oncall team
    # add an extra log message
    # incrementing counter
except TypeError as exp:
    print("Make sure that there two arguments and they are both numbers!")
    traceback.print_exc()
except Exception as exp:
    print("Something went wrong!")
    print(exp)
    traceback.print_exc()
else:
    print("Only if there wasn't an error!")
    print(result)
finally:
    print("This will always run - and allow for clean up!")