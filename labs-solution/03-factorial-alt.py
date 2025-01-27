print('Starting factorial calculation program')

number = ""

while not number.isnumeric():
    number = input('Please input the number: ')

num = int(number)

print(f'The number to calculate factorial for is {number}')
num = int(number)
if num == 0:  # Termination criteria
    print('0! factorial is 1')
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f'{number}! factorial is {factorial}')



