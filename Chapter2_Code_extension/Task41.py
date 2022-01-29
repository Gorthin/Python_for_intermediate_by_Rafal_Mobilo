#!/usr/bin/python3
import os
'''This time you work in a crazy research center.
Professors prepare their scripts and place them in a specific directory.
Your script is supposed to read these scripts and execute them one by one.
Below are two sample scripts. Copy and save each of them in a separate file.
Create a list containing the paths to the scripts:

files_to_process = [
    r "C:Python_math_sin_square.py"
    r "C:Pythonmath_square_root.py"
    ]
For each file:
display the file name (use the os.path.basename function from the os module)
open the file in question and read it into the source variable
Execute this script'''

files_to_process = [
    r"D:\Python\Python_for_intermediate_by_Rafal_Mobilo\Chapter2_Code_extension\math_sin_square.py",
    r"D:\Python\Python_for_intermediate_by_Rafal_Mobilo\Chapter2_Code_extension\math_square_root.py"
    ]

for file_path in files_to_process:
    with open(file_path, 'r') as f:
        print('File {} - '.format(os.path.basename(file_path)))
        source = f.read()
        exec(source)