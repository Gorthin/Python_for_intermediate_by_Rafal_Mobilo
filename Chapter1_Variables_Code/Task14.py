#!/usr/bin/python3

'''Create a function that takes a file path as a parameter and returns the number of words in that file.'''

import os


def count_words(path):
    with open(path, 'r') as f:
        content = f.read()
        word_count = len(content.split())
    return word_count


path = r'd:\Python\Python_for_intermediate_by_Rafal_Mobilo\Chapter1_Variables_Code\test.txt'
if os.path.isfile(path):
    print("There are {} words in the file {}".format(count_words(path), path))

os.path.isfile(path) and print("There are {} words in the file {}".format(count_words(path), path))