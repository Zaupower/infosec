'''
 Read a number from console and determine if it is a perfect square number. A perfect square is
a number that can be expressed as the product of an integer by itself or as the second exponent
of an integer.
    a. Hint: input() – built-in python function.
'''
import math
number = float(input('Insert a number\n'))

sqrt_number = math.sqrt(number)
if sqrt_number.is_integer():
    print("The number is a perfect square")
else:
    print("The number is not a perfect square")