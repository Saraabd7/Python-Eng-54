# For loops
# Syntax


# for item in iterable: mean something you can go over for e.g: list
# block of code:
import time
cool_cars = ['Skoda felicia fun', 'Fiat abarth the old one', 'toyota corola, Fiat panda 4x4', 'Fiat Multipla']


for car in cool_cars:
    print(car)


for lunch_time in cool_cars:
    print(car)
    time.sleep(1)

print('1 -', cool_cars[0])

Count = 0  # first number being used ( to do the count for points.
for car in cool_cars:
    print(Count + 1, '-', car)
    Count += 1

# For Loop for dictionaries:

boris_dict = {
    'name': 'boris',
    'l_name': 'Johnson',
    'phone': '0784171157',
    'address': '10 downing street'}
for item in boris_dict:
    print(item)
# this item is the key so we change it to key:
for key in boris_dict:
    print(key)
    # I want each individual values
    # for this i need, dictionary + key
    print(boris_dict[key])
    print(boris_dict['phone'])

# for key in boris_dict:
    # print(boris_dict['phone'])
    # print(boris_dict['name'])
for value in boris_dict.values():
    print(value)
    print('Name:', 'Boris Johnson')
    print('phone:', '0784171157')