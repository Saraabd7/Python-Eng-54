
# Exercise_104

# Section 1:

name = 'Lana'
last_name = 'Smith'
species = 'Female'
eye_color = 'Brown'
hair_color = 'Blond'

name = input('Enter a new name: ')
last_name = input('Enter a new last name: ')
species = input('Enter a new species: ')
eye_color = input('Enter a new eye color: ')
hair_color = input('Enter a new hair color: ')
age = int(input("Enter your age: "))

print(f'Hello {name} {last_name}. Your species are {species}, your eye color is {eye_color}, and hair is {hair_color}')
print(f'You said  your age is {age}. You were most likely born in ', 2020 - age)

# Section 2:
ame = input('Enter your name: ')
age = int(input('Enter your age: '))

m_name = input('Enter your mother name: ')
m_age = int(input('Enter your mother age: '))

print(f'Your name is {name}, and you are {age} born on the year of ', 2020 - age, '. This is a difference of ', m_age -
      age, 'later than your mother ', m_name, 'who was born on', 2020 - m_age)

