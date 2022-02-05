#!/usr/bin/env python3

'''
In this task you will write 2 generators which you will use to check URLs stored in files in one directory.
The benefit of this approach is that you have separate logic for retrieving the file names,
separate for reading the data, separate for checking the URL validity and finally separate for
tying it all together. By the way - a review of how to use the os and requests modules. Get to work!
Import the os and requests modules
Write a generator gen_get_files that takes a dir argument. The generator's task is to return,
one by one, all files from the directory given as dir parameter. (Use the os.listdir() function.
Return the full path to the file (use os.path.join()
https://docs.python.org/3/library/os.html

Write a generator gen_get_file_lines taking filename as argument. The purpose of the generator
is to return consecutive lines found in the file passed as filename parameter.  While returning
the result remove from the line the potential enter char occurring at the end of the line

Write function check_webpage which takes url argument.  Function's task is to fetch the page
specified by url argument. (To fetch the page use requests. get(...)). Return logical value from function.
If the status written as a result of response.get function call is equal 200, then return True.
In case of any other status or any error, return False.
Using the following code create a subdirectory in the c:/temp directory and in it 2 files:

try:
    os.mkdir('c:/temp/links_to_check')
except:
    pass

with open('c:/temp/links_to_check/en.txt', 'w') as f:
    f.write('http://www.wykop.pl/')
    f.write('http://www.ale-beka-jest-taki-adres.pl/')
    f.write('http://www.demotywatory.pl')

with open('c:/temp/links_to_check/com.txt', 'w') as f:
    f.write('http://www.realpython.com/')
    f.write('http://www.nonexistenturl.com/')
    f.write('http://www.stackoverflow.com')
For each file returned by the generator call gen_get_files('c:/temp/links_to_check')
and for each line returned by gen_get_file_lines(file)
call function check_webpage(line)
display a message on the screen in the form file - web address - True/False depending on whether the address is correct or not
'''

import os
import requests


def gen_get_files(dir):
    for d in os.listdir(dir):
        yield os.path.join(dir, d)


def gen_get_file_lines(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            yield line.replace('\n', '')


def check_webpage(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False


try:
    os.mkdir('D:\\1_PYTHON_PROJEKTY\\Python_for_intermediate_by_Rafal_Mobilo\\Chapter9_Generators\\links_to_check')
except:
    pass

with open('D:\\1_PYTHON_PROJEKTY\\Python_for_intermediate_by_Rafal_Mobilo\\Chapter9_Generators\\pl.txt', 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
    f.write('http://www.demotywatory.pl')

with open('D:\\1_PYTHON_PROJEKTY\\Python_for_intermediate_by_Rafal_Mobilo\\Chapter9_Generators\\com.txt', 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')

for file in gen_get_files('D:\\1_PYTHON_PROJEKTY\\Python_for_intermediate_by_Rafal_Mobilo\\Chapter9_Generators\\links_to_check'):
    for line in gen_get_file_lines(file):
        print("{} - {} - {}".format(file, line, check_webpage(line)))