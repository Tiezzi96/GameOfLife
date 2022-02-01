import sys
import os
import inspect
import pathlib
def get_base_path(base_file='constants.py',file_path=None):
    if file_path is None:
       file_path = os.getcwd()
    path_arr = file_path.split('/')
    base_path = '/'
    for path in path_arr:
        if path != '':
           base_path += "{}/".format(path)
           file = pathlib.Path(base_path+"/"+base_file)
           if file.exists():
              return base_path
    return 

