# Dictionaries
# it is organised by keys which it is values.
# Work with Keys and value Pairs.
# Work like a real dictionary, you just lookup the information for the specific key.
# The big differency with list is they are organised with index and here we use keys.
# We just make a list of cring_landlords, but we need more information. like there phone numbers and address.

# Syntax
# dic_variable_name = {'key':'value'}
boris_dict = {
    'name': 'boris',
    'l_name': 'Johnson',
    'phone': '0784171157',
    'address': '10 downing street'
}
print(boris_dict)
print(type(boris_dict))

# Access one key value pair
#  follow the same principle of list, but use keys not indexes.
print(boris_dict['name'])
# other way to do it:
last_name = boris_dict['l_name']
print(last_name)


# Change the value of on key value pair.

boris_dict['phone'] = '+7 9374749933'
print(boris_dict['phone'])
print(type(boris_dict['phone']))

# assign a new key value pair.
# assign home phone number for example:
print(boris_dict) # to See everything on the dictionary

boris_dict['home phone'] = '+44 456789876545'
print(boris_dict)

boris_dict['number_budgets_passed'] = 0
print(boris_dict['number_budgets_passed'])
print(boris_dict)
# the following two lines do exactly the same thing - increase the original value by 1
# accessing the value with the key, saving to variable
n_budget = boris_dict['number_budgets_passed']

#  adding + 1 to that vale
n_budget = n_budget + 1  # now its 1
n_budget += 1  # now its 2
print(n_budget)

# re assigning new value to the key
boris_dict['number_budgets_passed'] = n_budget

boris_dict['number_budgets_passed'] += 1  # now its 3
print(boris_dict['number_budgets_passed'])

# get all the keys
print(boris_dict.keys())

# get all the values
print(boris_dict.values())