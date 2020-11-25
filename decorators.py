#!/usr/bin/env python3

from functools import wraps


@wraps
def checker(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print("%s(%s) = %s" % (func.__name__,','.join(*args)),result)
        return result
    return inner


def add(a,b):
    return a + b
