#!/usr/bin/python3

'''
Here is a function that retrieves data from web pages:
import requests
import os

def save_url_file(url, dir, file,msg):

    print(msg.format(file))

    r = requests.get(url, stream = True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)


This can be called using the following code:
msg = "Please wait - the file {} will be downloaded"

url = 'http://mobilo24.eu/spis'
dir = 'c:/temp/'
file = 'spis.html'
save_url_file(url, dir, file,msg)

url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
dir = 'c:/temp/'
file = 'logo.png'
save_url_file(url, dir, file,msg)

For the project you are working on, the download directory
should always be the same (for example, let's assume c:/temp),
and the message displayed on the screen should always be "Please wait: {}"

Write a partial save_url_to_dir function that can only be
called with the arguments url and file
'''

import requests
import os
import functools


def save_url_file(url, dir, file, msg):
    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)


save_url_to_dir = functools.partial(save_url_file, dir='D:\Python\Python_for_intermediate_by_Rafal_Mobilo\Chapter4_Functions_scenarios', msg='Please wait: {}')

url = 'http://mobilo24.eu/spis'
file = 'spis.html'
save_url_to_dir(url=url, file=file)

url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
dir = 'D:\Python\Python_for_intermediate_by_Rafal_Mobilo\Chapter4_Functions_scenarios'
file = 'logo.png'
save_url_to_dir(url=url, file=file)