#!/usr/bin/env python3

from functools import wraps
from random import randint
from time import perf_counter, sleep


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


# Calculate the run time of a function
def timer(func):
    @wraps(func)
    def timer_wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.8f} seconds")
        return result
    return timer_wrapper


# A generic debug wrapper to display the function name and arguments
def debugger(func):
    @wraps(func)
    def debugger_wrapper(*args, **kwargs):
        args_repr = [repr(x) for x in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        result = func(*args, **kwargs)
        print(f"Calling {func.__name__}({signature}) = {result!r}")
        return result
    return debugger_wrapper


def add(a, b, c, d):
    return a + b + c + d

if __name__ == '__main__':
    add = debugger(add)
    help(add)
    a = randint(1, 30)
    b = randint(1, 30)
    c = randint(1, 30)
    d = randint(1, 30)    
    result = add(a, b, c, d)
    print("The result from add(%d,%d,%d,%d) is: %d" % (a, b, c, d, result))