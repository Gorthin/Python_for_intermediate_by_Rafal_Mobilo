#!/usr/bin/env python3

'''
As you can see this class is not a context manager, but we will change that:
import the contextlib module
change the line that creates an instance (f = FileFromWeb...) to a with statement
so that you use the closing method from the contextlib module to create a context manager
And now we're going to mess things up a bit... :
in the close method, comment out the if statement.
Let the instruction that deletes the file be executed unconditionally
run the code - it should work correctly
uncomment the last line that deletes the file. Run the script again, which should end with an error this time.
Let's fix it:
Put the with block added in the previous steps into another with block, which will "hide" the FileNotFoundError exception
'''

import os
import zipfile
import requests
import contextlib


class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def download_file(self):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self

    def close(self):
        # if os.path.isfile(self.tmp_file):
        os.remove(self.tmp_file)


with contextlib.suppress(FileNotFoundError):
    with contextlib.closing(
            FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'c:/temp/euroxref1.zip')) as f:
        f.download_file()

        with zipfile.ZipFile(f.tmp_file, 'r') as z:
            a_file = z.namelist()[0]
            print(a_file)
            os.chdir('c:/temp')
            z.extract(a_file, '.', None)

        os.remove(f.tmp_file)