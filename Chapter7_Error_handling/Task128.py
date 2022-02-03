#!/usr/bin/env python3

'''
Start the task with the solution from the previous lesson (if you don't have yours, you can use mine)
Handle the following error categories independently:
requests.exceptions.ConnectionError - you can easily provoke this error by entering an invalid URL
PermissionError - you can get this error by checking "read only" attribute of the index.html file
FileNotFoundError - this error can appear during attempts, when file download.tmp does not exist and file copy instruction is executed
Exception - general error handling "just in case".
When handling errors, simply display messages
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

except requests.exceptions.ConnectionError:
    print('Error downloading the file. The URL {} is incorrect'.format(url))

except FileNotFoundError:
    print('File cannot be found: {}'.format(tmpfile_path))

except PermissionError:
    print('Problem accessing a file: {}'.format(file_path))

except Exception as e:
    print('General Error downloading the URL {}'.format(url))
    print('Error details: {}'.format(e))

else:
    print('URL downloaded successfully {}'.format(file))

finally:
    if os.path.exists(tmpfile_path):
        print('Final removal of the file {}'.format(tmpfile_path))
        os.remove(tmpfile_path)
    print('DONE!')