#!/usr/bin/env python3

'''
Add error handling to this class in __exit__:
if you change the directory to a non-existent directory in the penultimate line, an error will be generated: FileNotFoundError
Just display the appropriate error message (hide the real reason)
if in the last line you ask the user to extract a non-existing file, an error will be generated: KeyError
Only display the appropriate error message (hide the real reason)
in other cases the error should be reported externally
Note: if the error occurs in the __enter__ method, the method shown in this
lesson will not work, because then the with block is not executed at all, so there is no __exit__ method
'''

import os
import zipfile
import requests


class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('>>>>>>>>>>> Error details', exc_type, exc_val, exc_tb)
        if exc_type == KeyError:
            print('>>>>> There is no file in archive! {}'.format(exc_val))
            return True
        elif exc_type == FileNotFoundError:
            print('>>>>> Incorrect directory/file: {}'.format(exc_val))
            return True
        else:
            return False


with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'c:/temp/euroxref.zip') as f:
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir('c:/temp')
        z.extract(a_file, '.', None)