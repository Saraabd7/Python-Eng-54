# Dictionary basics :D
# 1 - Define  a dictionary call story1, it should have the following_keys:
# 'Start', 'middle' and 'end'

story1_dict = {'Start': '',
               'Middle': '',
               'End': ''}


# 2 - print the entire directory
print(story1_dict)
# 3 - print the type of your directory
print(type(story1_dict))
# 4 - print only the keys
for keys in story1_dict:
    print(keys)
# 5 - print only the values
for values in story1_dict:
    print(values)
# 6 - print the individual values using the key (individually, lots of printi commands)
print(story1_dict['Start'])
print(story1_dict['Middle'])
print(story1_dict['End'])
# 7 - Now let's add a new key: value pair.
# 'hero': yourSuperHero
story1_dict['hero'] = 'yourSuperHero'
print(story1_dict)
