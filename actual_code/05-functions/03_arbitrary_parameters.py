def sum(a,b):
    return a + b

print(sum(1,2))

def sum_three(a,b,c):
    return a + b + c

print(sum_three(1,2,3))

def sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total

def product(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(sum())

def calculate(operation, *nums):  # ...
    if operation == "add":
        return sum(*nums)
    elif operation == "multiply":
        return product(*nums)
    else:
        print("Unhandled operation")
        return None

print(calculate( "add", 1,2,3,4,5))
print(calculate("multiply", 2,3,4,5,6,7))

print(*[1,2,3,4])