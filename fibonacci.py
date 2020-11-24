#!/usr/bin/env python3
from argparse import ArgumentParser
# Python program to display the Fibonacci sequence

DEFAULT_NTERMS = 10


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# The following are two recursive approaches
# The following runs in: O(N^2) time and O(N) space
# def getNthFib(n):
#     if n == 2:
#         return 1
#     elif n == 1:
#         return 0
#     else:
#         return getNthFib(n - 1) + getNthFib(n - 2)


# # The following runs in: O(N) time and O(N) space due to stack and memoize
# def getNthFib(n, memoize={1: 0, 2: 1}):
#     if n in memoize:
#         return memoize[n]
#     memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize)
#     return memoize[n]


# The following is an iterative solution
def getNthFib(n):
    last_two = [0, 1]
    counter = 3
    while counter <= n:
        next_fib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = next_fib
        counter += 1
    return last_two[1] if n > 1 else last_two[0]


if __name__ == '__main__':
    parser = ArgumentParser('This program will display a fibonacci sequence')
    parser.add_argument('-n','-nth-fib',dest='nthfib',help='Get the nth Fibonacci sequence',default=0,type=int)
    parser.add_argument(dest='nterms', help='The number of terms in the sequence',type=int,
                        default=DEFAULT_NTERMS, nargs='?')
    args = parser.parse_args()

    if args.nthfib > 0:
        print("The Fibonacci value for N (%d) is: %d" % (args.nthfib, getNthFib(args.nthfib)))
    else:
        print("Fibonacci sequence:")
        for i in range(args.nterms):
            print("%4d: %d" % (i + 1,fibonacci(i)))
