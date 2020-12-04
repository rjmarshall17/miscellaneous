#!/usr/bin/env python3

from functools import wraps


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


def add(x, y, a, b):
    return x + y + a + b


if __name__ == '__main__':
    add = checker(add)
    result = add(3, 4, b=5, a=10)
    print("The returned result is: %d" % result)
