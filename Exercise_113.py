# functions
# practice using, defining and calling functions
# Build a basic object functional calculator
# phase 1: build a function containing add, subtract, multiply, divide
# phase 2: find area of a circle, triangle and square

import math

def cal_add(x, y):
    return x + y
print(cal_add(3, 5))
def cal_subtract(x, y):
    return x - y
print(cal_subtract(12, 6))

def cal_multiply(x, y):
    return x * y
print(cal_multiply(4, 2))

def cal_divide(x, y):
    return x / y
print(cal_divide(18, 2))

def triangle_area(base, height):
  return 0.5 * base * height
print(triangle_area(10, 5))




def circle_area(radius):
    return (radius ** 2) * math.pi
print(circle_area(60))



def square_area(hight, length):
    return (hight * length)
print(square_area(4 , 4))


