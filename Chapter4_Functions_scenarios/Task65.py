#!/usr/bin/python3
import os
import functools
from datetime import datetime as dt


'''
You are working on an application that works intensively with files.
 The client has requested that each such operation be additionally logged. The log should be more or less like this:

Action FILE_CREATE executed on c:\dummy_file.txt on 2029-01-12 9:29:17

It is known that:
all these functions take one path parameter (so they may use the same wrapper)
the client may want to save the login data separately to a different file for each function (so the wrappers will differ slightly)
'''


def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            with(open(log_file_path, 'a')) as f:
                f.write('Action {} executed on {} on {}\n'.format(logged_action, path,
                                                                  dt.now().strftime("%Y-%m-%d %H:%M:%S")))

            return func(path)

        return the_real_wrapper

    return wrapper_with_log_to_known_file


@wrapper_with_log_file('FILE_CREATE', r'D:\1_PYTHON_PROJEKTY\Python_for_intermediate_by_Rafal_Mobilo\Chapter4_Functions_scenarios\file_create.txt')
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")


@wrapper_with_log_file('FILE_DELETE', r'D:\1_PYTHON_PROJEKTY\Python_for_intermediate_by_Rafal_Mobilo\Chapter4_Functions_scenarios\file_delete.txt')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(r'D:\1_PYTHON_PROJEKTY\Python_for_intermediate_by_Rafal_Mobilo\Chapter4_Functions_scenarios\dummy_file.txt')
delete_file(r'D:\1_PYTHON_PROJEKTY\Python_for_intermediate_by_Rafal_Mobilo\Chapter4_Functions_scenarios\dummy_file.txt')
create_file(r'D:\1_PYTHON_PROJEKTY\Python_for_intermediate_by_Rafal_Mobilo\Chapter4_Functions_scenarios\dummy_file.txt')
delete_file(r'D:\1_PYTHON_PROJEKTY\Python_for_intermediate_by_Rafal_Mobilo\Chapter4_Functions_scenarios\dummy_file.txt')