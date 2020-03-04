
#
#While_loops
# syntex
# while <condition>:
    # run block of code
    # if <condition>:
        #break
# counter = 0
#
# while counter <= 10:
#     print(counter)
#     print('this is cool')
#     counter = counter + 1
#
# user_input = input('you want to play?')
#
# while user_input == 'yes' or user_input == 'y':
#     random_num = 10
#     print('welcome to out random game')
#     user_input = input('what is your guess? ')
#     if user_input == random_num:
#         print('WELL DONE! WELL DONE')
#     else
#         print('sorry youwhere wrong')
#     user_input = input('play again')

# reserved words
#break - used to break the while loop
# continue - skips to the next iteration without running the following code/ blocks

user_input = input('you want to play?')
while user_input == 'yes' or user_input == 'y':...
while True:
    user_input = input('choose 1 for pancakes, 2 for cakes, 3 to exit.. or just exit')
    if user_input == '1':
        print('pancakes!')
        print('plus what ever pancake logic you have')
    elif user_input == '2':
        print('cakes!')
    elif 'exit' in user_input or user_input == '3':
        print('goodbye')
        break
    else:
        print(' USE YOUR NUMBER AND YOUR KEYBOARD...')
