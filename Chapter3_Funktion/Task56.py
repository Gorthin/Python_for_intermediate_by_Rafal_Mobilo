#!/usr/bin/python3

'''The following functions are given:
Write a function that becomes a common interface for these functions.
Let the new function be called generate_values and:
takes as its first argument the function name (one of the above)
as second argument it takes a list of numbers, for which value should be determined
this function should generate a value for each value in the list from
the previous point and return the list with the results'''


def double(x):
    return 2 * x


def square(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


def generate_values(how, x_table):
    value_list = []

    for x in x_table:
        value_list.append(how(x))

    return value_list


x_table = list(range(11))

print(generate_values(double, x_table))
print(generate_values(square, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))