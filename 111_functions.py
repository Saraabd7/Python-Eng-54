# Functions
# A function is like a machine
#
# it can take in inputs
# and do some work (block of code)
# and it can output something different
#  they need to be called to work

# Calling a function is just writing the name and passing the arguments it needs

# functions - good practices
# they do ONE job
# they should be testable and maintainable
# good naming convention
# Generally NEVER print inside a function
# inside a function your return()

#### the above avoids STRING code - Spaguetti code
# reduce technical debt

# concept of DRY
# Don't
# Repeat
# Yourself

# Syntax
# def name_of_function(arg1, arg2):
#     # block of code
#     #
#     return 'doing some work'
# defining a simple function
def say_hello_zeus():
    # print('I like python') bad :)
    return('hello Zeus')

# calling but not printing
# say_hello_zeus()
# 'hello zeus'

# calling AND printing a function
# print(say_hello_zeus())


# defining a function with arguments
## arguments are variables that exist in the scope of a function

def full_name_formater(f_name, l_name):
    # Format each name nicely
    # I can use .strip and . cpitalized
    # I have access to the name via the arguments f_name and l_name
    # save these into variables
    formated_f_name = f_name.strip().capitalize()
    formated_l_name = l_name.strip().capitalize()

    # return a joined full name that is correctly formatted
    # join the two variable into one string
    full_name = formated_f_name + ' ' + formated_l_name
    # return said string
    return full_name

# call function with names
print(full_name_formater(' SHAnnon  ', '    GreyhOUnd'))


def add_funt(num1 = 10 , num2 = 300):
    # I want to return the addition of two numbers
    # I have acces to num1 and num2 I can add them
    # I can save result in a variable
    result = num1 + num2
    # I can return said variable
    return result

# calling funtion with two arguments
print(add_funt(10, 300))



