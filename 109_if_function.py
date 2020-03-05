# if_functions
# syntax
# if <condition>:
# block of code  that runs if condition return true.
# Notes:
# if functions will exit once a condition becomes true
# build your if function with the most specific thing at the top


weather = 'rainy'
if weather == 'rainy':
    print('Take your umbrella')

# # it won't print when the value is different
# weather = 'Sunny'
# if weather == 'rainy':
#     print('Take your umbrella')

weather = 'Sunny'
if weather == 'rainy':
    print('Take your umbrella')
elif weather == 'Sunny':
    print('nice, take some shades B')
else: print("didn't quit catch that sport, could you repeat")

weather = 'Fish finger Sandwich'
if weather == 'rainy':
    print('Take your umbrella')
elif weather == 'Sunny':
    print('nice, take some shades B')
else:
    print("Didn't quit catch that sport, could you repeat")

# if i have to condition almost the same like this example they asked if the weather is rainy in 2 of if conditions:


weather = 'very rainy and very windy'
if 'rainy' in weather:
    print('Take your umbrella')
elif weather == 'Sunny':
    print('nice, take some shades B')
elif 'rainy' in weather and 'windy' in weather:
    print('it looks bad, stay in')
else:
    print("Didn't quit catch that sport, could you repeat")
    # it will print the first one because if it been checked and found the condition will print the first one.

# if 'rainy' in weather and 'windy' in weather:
#     print('it looks bad, stay in')
# if 'rainy' in weather:
#     print('Take your umbrella')



