#!/usr/bin/env python3
from argparse import ArgumentParser
from memory_profiler import profile

"""
This is a simple recursive, maybe also iterative?, example of factorial
n! = n * (n - 1) * (n - 2) * (n - 3) *...
n! = n * (n - 1)!
"""


@profile
def factorial(n):
    if n <= 1:
        return 1
    return n * (factorial(n -1))


@profile
def iterative_factorial(n):
    if n == 0:
        return None
    if n <= 1:
        return 1
    total = 1
    while n > 0:
        # print('n=%d total=%d' % (n,total))
        total = total * n
        n -= 1
    return total


if __name__ == '__main__':
    parser = ArgumentParser('Simple factorial script')
    parser.add_argument('-i','--iterative',dest='iterative',help='Use the iterative function',default=False,
                        action='store_true')
    parser.add_argument(dest='n_factorial',help='Calculate n!',default=0,type=int,nargs='?')
    args = parser.parse_args()

    if args.iterative:
        print(iterative_factorial(args.n_factorial))
    else:
        print(factorial(args.n_factorial))
