from distutils.log import error
import sys

def throw_error(msg, to_exit=False):
    print(msg, file=sys.stderr)
    error(msg, file=sys.stderr)
    if to_exit:
        exit()