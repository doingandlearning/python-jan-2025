# anonamous functions that we assign to variables or define as we need them

def sum(a,b):
    # can do some work
    # call out to some api
    #
    return a + b

print(sum(1,2))

sum = lambda a, b: a + b  # implicit return

print(sum(1,2))