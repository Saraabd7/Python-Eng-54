# Exercise_106

import random
magic_number = random.randint(1, 10)
user_num = 0

tries = 3

while tries != 0:
    #while user_num != magic_number:
    user_num = int(input('Guess the number: '))
    if user_num == magic_number:
        print(f'Congratulations, you guessed the number, Thank you for playing')
        break
    elif user_num > magic_number:
        print('Too high!')
        tries -= 1
        continue
    elif user_num < magic_number:
        print('Too low!')
        tries -= 1
        continue

if user_num != magic_number:
    print("Sorry, but you didn't manage to guess the number")
