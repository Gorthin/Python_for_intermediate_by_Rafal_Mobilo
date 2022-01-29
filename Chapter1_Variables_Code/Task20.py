#!/usr/bin/python3

'''In this task, save the contents of several web pages to disk. When the download is complete, display a success message. However, if there is an error, display an error message and break the loop.

For each page of pages:
-store in the path variable the path to the file formed by combining data_dir, the name of the page retrieved from pages, and ".html"
-Using the urllib.request.urlretrieve(<page address>, <path to file> function), save the page to disk
-inside the for loop add a try/except block, which in case of an error will terminate the loop by displaying an error message

Translated with www.DeepL.com/Translator (free version)'''


import os
import urllib.request

data_dir = r'd:\Python\Python_for_intermediate_by_Rafal_Mobilo\Chapter1_Variables_Code\Task20'
pages = [
    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},

    { 'name': 'learngitbranching', 'url': 'https://learngitbranching.js.org/' },

    { 'name': 'learnhtmlcss',       'url': 'https://learn.shayhowe.com/html-css/'},

    { 'name': 'exercisespython',       'url': 'https://pl.spoj.com/'} ]

for page in pages:

    try:
        file_name = "{}.html".format(page["name"])
        path = os.path.join(data_dir, file_name)

        print("Processing: {}  => {} ...".format(page["url"], file_name))
        urllib.request.urlretrieve(page["url"], path)
        print('...done')

    except:
        print('FAILURE processing web page: {}'.format(page["name"]))
        print('Stopping the process!')
        break

else:
    print('All pages downloaded successfully!!!')