#!/usr/bin/env python3

'''
Here you have been given a special assignment. You need to write a class that will be responsible for:
downloading a zip file from the Internet
saving it in the specified location
Your new class is to be used as a Context Manager. The current plan is to download the
zip file and unzip its contents, but this is already supposed to happen in
the Context Manager outside the class. If you know how to do this, then go ahead, and if you want more detailed instructions then see:
import the os, zipfile and requests modules
define the FileFromWeb class
in the __init__ method accept and store the parameters
url - containing the address of the file to download
tmp_file - indicating where the file should be saved
in the __enter__ method
save the result of the requests.get(self.url) call to the response variable
open for saving in binary mode the file pointed by the path self.tmp_file
write response.content to this file
return the self object
do nothing in the __exit__ method
use the class by writing an expression with:
create an instance of FileFromWeb class using the arguments (if the web address didn't respond, change it to any other zip file):
https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip
c:/temp/euroxref.zip
give the instance the alias f
in the with block create another with statement - create an instance of the zipfile.ZipFile class - pass as arguments:
f.tmp_file - which is the path to the locally stored zip file
"r" - information that the file will be opened for reading
give the object the alias z
object in the with block:
get the name of the first file found in the zip archive using the z.namelist()[0] method. Store the result in the a_file variable
display the a_file variable (for control purposes only)
change the current directory to one of your choice, e.g. c:/temp - use the chdir method of the os module
extract the file using the z object method named extract. The arguments are:
the name of the file to extract - here a_file
the name of the directory to extract the file to - pass a dot
the password to open the archive - pass None
Run and test the program!
'''


import os, zipfile, requests

class FileFromWeb:

    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file

    def __enter__(self, response):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'c:/temp/euroxref.zip') as f:
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir('D:\\1_PYTHON_PROJEKTY\\Python_for_intermediate_by_Rafal_Mobilo\\Chapter10_Context_Manager')
        z.extract(a_file, '.', None)