# practice string
# welcome to sparta -exercise

# version 1 Specs  with concatenation
# define  a variable name , and assign a string.

name = 'sara'
print('sara')


# prompt the user for input and ask the user for his/her name.
person = input('What is your name ?')
print('name', person)
# re assign the original variable this input

# use  concatenation to print a welcome message and use method to format the name/ input (remove white spaces)

print('WELCOME {} TO OUR CLASS'. format(name))

# version 2: with interpolation

# ask the user for a first name, save it  in a variable.
# ask the user for a last name, save it  in a variable.
# use interpolation to print the message.
firstname = input("Input your First Name : ")
lastname = input("Input your Last Name : ")
print("Hello" + " " + firstname + " " + lastname);


# Calculate year of birth
# gather details on age and name
# print something like
# OMG <person>, you are <age> years old so you were born in <year>


print('OMG Maria you are <> years old so you were born in 1994')
