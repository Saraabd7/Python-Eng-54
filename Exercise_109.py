# Exercise_109:


while True:
    age = int(input('What is your age? '))
    driver_license = input('Do you have a driving licence? (Yes/No):')
    if (age >= 18) and (driver_license == 'Yes'):
        print('You can vote and drive')
    elif (age >= 16) and (age < 18):
        print("you can't legally drink but your mates/uncles might have your back")
    elif age >= 18:
        print('You can vote')
    elif driver_license == 'Yes':
        print('You can drive')
    elif age < 18:
        print("You're too young, go back to school!")
    elif driver_license == 'exit':
        break
        print('Thank you')






















































