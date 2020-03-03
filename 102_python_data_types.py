# Strings
# Text and Characters
# Syntax
# "" and ''

# Define a string
my_string = 'Hey I am a cool String B'
print(my_string)


Check it type:

print (type(my_string))


# Conacatenation
## Adding of two strings
joint_string = my_string + 'This is another string'
print(joint_string)

Example 2:


name='mohamad'
Welcome_text = 'WELCOM TO SPARTAAAAA(300)'
PRINT(Welcome_textLCOME_TEXT + '' +name)
PRINT(welcome_text,name) #Overloading the print method






# Interpolation
## Inserting  a string inside another string or running python inside  a string
printing (f'WELCOME {(input" what is your name")}) TO OUR CLASS 54, WE ARE CONTESTED_ Terrain')
printing ('WELCOME {} TO OUR CLASS 54, WE ARE CONTESTED_ Terrain' . format(name))


# Usefull Methods
# Are like function but belong to specific data type
## Foe example, it would not make sence to try to capitalize integers
#Methods require the brakets at the end.
example_long str = 'Hello, This  is a very badly formated text?'
print (example_long_str)


Removing trailling white spaces
print(example_long_str.strip())
- Make it lower case
print(example_long_str.lower())
- Make it UpperCase
print(example_long_str.upper())
- Make only the first Character Capitalized
print(example_long_str.capitalized())
- Make the first character of each word capitalized
print(example_long_str.title ())
- Make the '?' into a '!'
print(example_long_str.replace('?','!'))

# Chain some methods and:


-Remove trailling White spaces

- Make it nicely formated with only the first letter capitalized

print(example_long_str.strip().caitalize().replace('?','!'). replace ('badly', 'well'))
# Create a list with individual words
#split() list
print (example_long_str.split())
