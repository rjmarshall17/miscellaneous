#!/usr/bin/env python3

from functools import wraps
from random import randint
from time import perf_counter, sleep


# The following is a generic template
def decorator(func):
    @wraps(func)
    def decorator_wrapper(*args, **kwargs):
        # do something before
        wrapper_result = func(*args, **kwargs)
        # do something after
        return wrapper_result
    return decorator_wrapper


def checker(func):
    @wraps(func)
    def inner(*args, **kwargs):
        all_args = ''
        wrapped_result = func(*args, **kwargs)
        all_args = ','.join([str(x) for x in args])
        if len(kwargs) > 0:
            if len(args) > 0:
                all_args += ","
            all_args += ','.join(["%s=%s" % (k, v) for k, v in kwargs.items()])
        print("%s(%s) = %s" % (func.__name__, all_args, wrapped_result))
        return wrapped_result
    return inner


# Calculate the run time of a function
def timer(func):
    @wraps(func)
    def timer_wrapper(*args, **kwargs):
        start_time = perf_counter()
        timer_result = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.8f} seconds")
        return timer_result
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


def add1(x, y, a, b):
    return x + y + a + b


def add2(xx, yy, aa, bb):
    return xx + yy + aa + bb


if __name__ == '__main__':
    def add(x, y, aa, bb):
        return x + y + aa + bb

    add1 = checker(add1)
    result = add1(3, 4, b=5, a=10)
    print("The returned result is: %d" % result)

    add2 = timer(debugger(add2))
    help(add2)
    a = randint(1, 30)
    b = randint(1, 30)
    c = randint(1, 30)
    d = randint(1, 30)    
    result = add2(a, b, c, d)
    print("The result from add(%d,%d,%d,%d) is: %d" % (a, b, c, d, result))
