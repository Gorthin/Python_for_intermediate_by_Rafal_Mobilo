#!/usr/bin/python3

'''Create a file and type some words into it, such as what you see outside your window :)
Create a function that takes the file path as a parameter and returns the number of words in that file, if you need help steps here they are:
Open the file with the open command (you can use the encoding="utf-16" parameter if you need to)
Read the file into a variable using the read() function
"Break" the loaded content using split() function
Count how many elements are returned by the split() function
Return that value
In the main script:
declare the variable path and assign it a value pointing to the file created at the beginning
write a conditional command to check if the file exists
if yes, call the function, count the number of words in the file and display information about it
write a logical expression that will perform the same actions as the previously written if statement
Translated with www.DeepL.com/Translator (free version)'''

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