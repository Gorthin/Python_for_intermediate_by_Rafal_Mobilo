#!/usr/bin/env python3

'''
Write a try/except/else/finally block that:
in the try block
if file tmpfile_path exists it will delete it
using save_url_to_file function will download the page from url into tmpfile_path file
copy the tmpfile_path file to the file_path
in case of errors, execute the except block, and in it:
display information about the error, including exception details
in the else block display the success message
in the finally block
delete the tmpfile_path if it exists
display message
Test the program with correct and incorrect url. Check the results displayed on the screen
'''

import requests
import os
import shutil


def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
dir = r'D:\\1_PYTHON_PROJEKTY\\Python_for_intermediate_by_Rafal_Mobilo\\Chapter7_Error_handling\\'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.exists(tmpfile_path):
        print('Removing {}'.format(tmpfile_path))
        os.remove(tmpfile_path)

    print('Downloading url {}'.format(url))
    save_url_to_file(url, tmpfile_path)

    print('Copying file {} {}'.format(tmpfile_path, file_path))
    shutil.copy(tmpfile_path, file_path)

except Exception as e:
    print('Error downloading the URL {}'.format(url))
    print('Error details: {}'.format(e))

else:
    print('URL downloaded successfully {}'.format(file))

finally:
    if os.path.exists(tmpfile_path):
        print('Final removal of the file {}'.format(tmpfile_path))
        os.remove(tmpfile_path)
    print('DONE!')