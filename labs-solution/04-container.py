readings = []
continue_to_enter_data = True
while continue_to_enter_data:
    input_string = input('Please enter a temperature reading (-1 to end): ')
    if input_string == '-1':
        continue_to_enter_data = False
    elif input_string.count('.') > 1 or not input_string.replace('.', '').isdigit():
        print('Must be a positive floating point number')
    else:
        reading = float(input_string)
        readings.append(reading)

print(f'Temperature readings input: {readings}')
print(f'There are {len(readings)} readings in total')

readings.sort()
print(f'Temperature readings sorted: {readings}')

readings.reverse()
print(f'Temperature readings in reverse: {readings}')

print(f'There are {readings.count(0.0)} zero readings')

readings_copy = readings.copy()
print(f'Copy of temperature readings: {readings_copy}')

readings_copy.append(5.5)
print(f'Temperature readings: {readings}')
print(f'Copy of temperature readings: {readings_copy}')

print(f'Popping element from end of copy list {readings_copy.pop()}')
print(f'Readings copy now contains {readings_copy}')
