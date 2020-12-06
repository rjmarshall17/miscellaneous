#!/usr/bin/env python3

import os
from heapq import heappush, heappop

"""
The median of a set of integers is the midpoint value of the data set for which an equal number of
integers are less than and greater than the value. To find the median, you must first sort your set
of integers in non-decreasing order, then:

o If your set contains an odd number of elements, the median is the middle element of the sorted sample.
  In the sorted set {1,2,3}, 2 is the median.

o If your set contains an even number of elements, the median is the average of the two middle elements
  of the sorted sample. In the sorted set {1,2,3,4}, (2+3)/2=2.5 is the median.

Given an input stream of n integers, you must perform the following task for each i-th integer:

1. Add the i-th integer to a running list of integers.
2. Find the median of the updated list (i.e., for the first element through the i-th element).
3. Print the list's updated median on a new line. The printed value must be a double-precision
   number scaled to  decimal place (i.e., 12.3 format).

Input Format

The first line contains a single integer, n, denoting the number of integers in the data stream.
Each line i of the n subsequent lines contains an integer, a-sub-i, to be added to your list.

Constraints

1 <= n <= 10**5
0 <= a-sub-i <= 10**5

Output Format

After each new integer is added to the list, print the list's updated median on a new line as a single
double-precision number scaled to 1 decimal place (i.e., 12.3 format).

Sample Input

6
12
4
5
3
8
7

Sample Output

12.0
8.0
5.0
4.5
5.0
6.0

Explanation

There are n = 6 integers, so we must print the new median on a new line as each integer is added to the list:

1. List = {12}, median = 12.0
2. List = {12,4} -> {4,12}, median = (4 + 12)/2 = 8.0
3. List = {12,4,5} -> {4,5,12}, median = 5.0
4. List = {12,4,5,3} -> {3,4,5,12}, median = (4 + 5)/2 = 4.5
5. List = {12,4,5,3,8} -> {3,4,5,8,12}, median = 5.0
6. List = {12,4,5,3,8,7} -> {3,4,5,7,8,12}, median = (5 + 7)/2 = 6.0
"""

#
# Complete the runningMedian function below.
#

###################################################################
# Python heaps are always min heaps, therefore to create a max heap
# you have to negate the value
###################################################################


def add_number(number, minheap, maxheap):
    if not maxheap or number < -maxheap[0]:
        heappush(maxheap, -number)
    else:
        heappush(minheap, number)


def balance_heaps(minheap, maxheap):
    if len(minheap) - len(maxheap) >= 2:
        heappush(maxheap, -heappop(minheap))
    if len(maxheap) - len(minheap) >= 2:
        heappush(minheap, -heappop(maxheap))


def get_median(minheap, maxheap):
    if len(minheap) == len(maxheap):
        return (minheap[0] - maxheap[0])/2
    elif len(minheap) > len(maxheap):
        return float(minheap[0])
    return float(-maxheap[0])


def running_median(incoming_array):
    results = []
    minheap = []
    maxheap = []
    for number in incoming_array:
        # Add the number to the most appropriate heap
        add_number(number, minheap, maxheap)
        # Balance the heaps, never more than 1 extra value per heap
        balance_heaps(minheap, maxheap)
        # Get the new median value and add to results
        results.append(get_median(minheap, maxheap))
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = running_median(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

    expected_output = os.environ['OUTPUT_PATH'].replace('output','expected_output')
    assert open(os.environ['OUTPUT_PATH'], 'r').read() == open(expected_output,'r').read()
    print("The expected output from %s matches the output in %s" % (expected_output,
                                                                    os.environ['OUTPUT_PATH']))
