#!/usr/bin/python3

'''In this task, you will build a process to build a string for transforming numeric data.

1 Create the following functions in your script:
2 Define number with value 8
3. define a list of transformations consisting of functions:
double
square
div2
negative
4. enter the value number into the temporary variable tmp_return_value
Write a loop that
goes through all items of the transformations list
each time calls the appropriate function, passing to it the current value of the tmp_return_value argument
displays the current value of the tmp_return_value variable
6. test the script also for the list of transformations with operations:
square
square
div2
double
'''


def double(x):
    return 2 * x


def square(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2

number = 8
transformations = [double, square, negative, div2]
tmp_return_value = number

print('Starting transformations')
for transformation in transformations:
    tmp_return_value = transformation(tmp_return_value)
    print('{}: temporal result is {}'.format(transformation.__name__, tmp_return_value))

number = 100
transformations = [square, square, div2, double]

print('Starting transformations')
tmp_return_value = number
for transformation in transformations:
    tmp_return_value = transformation(tmp_return_value)
    print('{}: temporal result is {}'.format(transformation.__name__, tmp_return_value))