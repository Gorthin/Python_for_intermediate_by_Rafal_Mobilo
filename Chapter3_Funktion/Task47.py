#!/usr/bin/python3

'''Write a function show_progress that will display
the line of text resulting from repeating a given
number of times a specified character. Function:
accepts a character argument that specifies what character is to be repeated
accepts how_many argument which specifies how many times a character should be repeated
the default value for character is an asterisk'''


def show_progress(how_many, character='*'):
    line = character * how_many
    print(line)


show_progress(10)
show_progress(15)
show_progress(30)

show_progress(10, '-')
show_progress(15, '+')