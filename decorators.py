#!/usr/bin/env python3

from functools import wraps
from random import randint


# The following is a generic template
def decorator(func):
    @wraps(func)
    def decorator_wrapper(*args, **kwargs):
        # do something before
        result = func(*args, **kwargs)
        # do something after
        return result
    return decorator_wrapper


def print_function(func):
    # @wraps wraps the inner function in order to preserve the name of the
    # wrapped/decorated function
    
	@wraps(func)
	def inner(*args, **kwargs):
		result = func(*args, **kwargs)
        
        # In order to join *args, you have to convert it to a list
        # and make sure all of the elements are strings
		print("%s(%s) = %s" % (func.__name__,
                               ', '.join([str(x) for x in list(args)]),
                               result))
		return result
	return inner


def add(a, b, c, d):
    return a + b + c + d

if __name__ == '__main__':
    add = print_function(add)
    help(add)
    a = randint(1, 30)
    b = randint(1, 30)
    c = randint(1, 30)
    d = randint(1, 30)    
    result = add(a, b, c, d)
    print("The result from add(%d,%d,%d,%d) is: %d" % (a, b, c, d, result))