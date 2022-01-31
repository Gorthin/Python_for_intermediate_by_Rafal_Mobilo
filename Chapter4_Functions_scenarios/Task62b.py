#!/usr/bin/python3
import time
import functools

'''
You work at SZIN (Super Crazy Institute of Science).  At SZIN,
a lot of importance is placed on making functions run fast!
That's why the idea came up that every strategic function
should have a wrapper that will measure the execution time of the function.

Here is the function for which you need to create a wrapper:

def get_sequence(n):

    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v

Translated with www.DeepL.com/Translator (free version)
'''


def wrapper_time(a_function):
    def a_wrapped_function(*args, **kwargs):
        time_start = time.time()
        print("Function {} started at {}".format(a_function.__name__, time_start))
        v = a_function(*args, **kwargs)
        time_stop = time.time()
        print("Function {} returned at {}".format(a_function.__name__, time_stop - time_start))
        return v
    return a_wrapped_function


@wrapper_time
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v


print(get_sequence(30))