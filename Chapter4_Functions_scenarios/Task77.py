#!/usr/bin/python3

'''
In this task, you will work with the following list:

text_list = ['x','xxx','xxxxx','xxxxxxx','']

1. prepare and store in the variable f a lambda function which
for an argument which is a text will return its length
2. test the function on any string
3. run the function f on each element of the text_list.
You will use the map function, which allows you to run
the function pointed to by the first argument for the list passed as the second argument.
Note: the map function does not return a list, but the
returned object can be easily converted to a list.

Change the map function call so that the function is
not stored in the variable f, but instead is defined dynamically in the map function call
'''

f = lambda x: len(x)

print(f('a 19-letters string'))

text_list = ['x', 'xxx', 'xxxxx', 'xxxxxxx', '']

print(list(map(f, text_list)))

print(list(map(lambda s: len(s), text_list)))