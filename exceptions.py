"""
    file to show how to handle exception
"""
import  os
import sys

def cconvert_to_int(x):
    """ convert an integer     """
    s = -1
    try:
        s = int(x)
        print('convertion success')
    except (ValueError, TypeError):
        pass
    return s

def make_at(path, dir_name):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        os.mkdir(dir_name)
    except OSError as e:
        print(e, file=sys.stderr)
        raise
    finally:
        os.chdir(original_path)