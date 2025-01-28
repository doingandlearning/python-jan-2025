def square(n: int | float):
    # do some work!
    return n * n
    # return n ** 2


answer = square(4)

print(answer)
print(square(-1))

if square(3) < 15:
    print("Maths works!")

print(f"10 squared is {square(10)}")


def return_three_things():
    return "Hello", 1, True

result = return_three_things()
print(result)

greeting, ice_cream_scoops, is_raining = return_three_things()  # unpacking
print(greeting)

def swap(a,b):
    return b, a

a = 2
b = 3
x,y = swap(a,b)

print(x,y)

