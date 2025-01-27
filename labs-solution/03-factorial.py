print('Starting factorial calculation program (type q to quit)')


while True:
    number = input('Please input the number: ')
    if number == "q" or number == "quit":
        break
    if number.isnumeric():
        print(f'The number to calculate factorial for is {number}')
        num = int(number)
        if num == 0:  # Termination criteria
            print('0! factorial is 1')
        else:
            # Loop element
            factorial = 1
            for i in range(1, num + 1):
                factorial = factorial * i
            print(f'{number}! factorial is {factorial}')
    else:
        print('Not an integer number')