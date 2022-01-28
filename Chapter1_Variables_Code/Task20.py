#!/usr/bin/python3

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