# Exercise_108:


# Dictionary basics :D
# 1 - Define  a dictionary call story1, it should have the following_keys:
# 'Start', 'middle' and 'end'

story1_dict = {'Start': 'Superman, Man of Steel ',
               'Middle': 'superman one of the most popular characters'
                         'he has most of normal superpowers like flight, strength, speed etc.',
               'End': ' Superman still one of the most comic book characters of all time.'}


# 2 - print the entire directory
print(story1_dict)
# 3 - print the type of your directory
print(type(story1_dict))
# 4 - print only the keys
print(story1_dict.keys())
# 5 - print only the values
print(story1_dict.values())
# 6 - print the individual values using the key (individually, lots of printi commands)
print(story1_dict['Start'])
print(story1_dict['Middle'])
print(story1_dict['End'])
# 7 - Now let's add a new key: value pair.
# 'hero': yourSuperHero
story1_dict['hero'] = 'Supermaaaan'
print(story1_dict)
