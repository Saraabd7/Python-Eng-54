# functions
# practice using, defining and calling functions
# Build a basic object functional calculator
# phase 1: build a function containing add, subtract, multiply, divide
# phase 2: find area of a circle, triangle and square

import math
x = int(input('Enter your first number: '))
y = int(input('Enter your second number: '))

def cal_add(x, y):
    return x + y
print(cal_add(x, y))
def cal_subtract(x, y):
    return x - y
print(cal_add(x, y))

def cal_multiply(x, y):
    return x * y
print(cal_add(x, y))
def cal_divide(x, y):
    return x / y
print(cal_divide )
print(cal_add(x, y))


def triangle_area(base, height):
  return 0.5 * base * height
print(triangle_area(x, y))

def circle_area(radius):
    return (radius ** 2) * math.pi
print(circle_area(x))

def square_area(hight, length)
    return (hight * length)
print(square_area(x * y))




