import sys

DEBUG = "-d" in sys.argv


def debug_print(*args, **kwargs):
    condition = kwargs.get('condition', True)
    if DEBUG and condition:
        print(*args)
