#!/usr/bin/env python3

'''
A system administrator would like to know how many files and directories are in a specific directory.
He's heard that this can be done in Python, and he's actually right...
Import the os module and itertools
Write a scantree generator that:
takes as argument the path to the initial path directory
then for each object returned by os.scandir:
(see documentation - https://docs.python.org/3/library/os.html#os.scandir -
objects returned by os.scandir are objects of class os.DirEntry - https://docs.python.org/3/library/os.html#os.DirEntry)
if this object is a directory, i.e. the is_dir() method of the object returns True
returns this object using yield
recursively calls scandir for this directory
if the object is a file, the is_dir() method returns False
returns the object using yield
Test this function on a not too large directory of your choice:
write the result of the scantree call to the variable listing, pointing with the argument to the selected directory
then go through the listing with a for loop and for each object display information about whether it is
a file or a directory and the full path to this file/directory
Using the groupby function from the itertools module, display information about the number of
directories and files in your chosen base directory. Remember to re-create the
listing variable sorting the listing object
'''


import os,itertools


def scantree(path):
    for entry in os.scandir(path):
        if entry.is_dir():
            yield entry
            yield from scantree(entry.path)
        else:
            yield entry


listing = scantree('C:/temp')
for l in listing:
    print('DIR ' if l.is_dir() else 'FILE', l.path)

listing = scantree('C:/temp')
listing = sorted(listing, key=lambda e: e.is_dir())

for is_dir, elements in itertools.groupby(listing, key=lambda e: e.is_dir()):
    print('DIR ' if is_dir else 'FILE', len(list(elements)))