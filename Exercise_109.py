age = 19
driver_lisence = True

while True:
    if age >= 19 and driver_lisence:
        print('You can vote and drive')
    elif age >= 19:
        print('You can vote')
    elif driver_lisence:
        print('you can drive')
    elif age > 16:
        print("you can't legally drink but your mates/uncles might have your back")

    else:
        print('Your too young, go back to school!')

