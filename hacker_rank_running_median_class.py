#!/usr/bin/env python3

import os
from heapq import heappush, heappop


class RunningMedian:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        
    def add_number(self, number):
        if not self.max_heap or number < -self.max_heap[0]:
            heappush(self.max_heap, -number)
        else:
            heappush(self.min_heap, number)
        self.__balance_heaps__()

    def __balance_heaps__(self):
        if len(self.min_heap) - len(self.max_heap) >= 2:
            heappush(self.max_heap, -heappop(self.min_heap))
        if len(self.max_heap) - len(self.min_heap) >= 2:
            heappush(self.min_heap, -heappop(self.max_heap))

    def median(self):
        if len(self.min_heap) == len(self.max_heap):
            # Because the self.max_heap contains negative numbers, we subtract,
            # i.e. add, the value from the self.max_heap to the value from the
            # self.min_heap and then divide by 2.
            return (self.min_heap[0] - self.max_heap[0])/2
        elif len(self.min_heap) > len(self.max_heap):
            return float(self.min_heap[0])
        # Again, the self.max_heap contains negative numbers in order
        # to allow a self.min_heap to work as a self.max_heap.
        return float(-self.max_heap[0])


def running_median(incoming_array):
    results = []
    rm = RunningMedian()
    for number in incoming_array:
        rm.add_number(number)
        results.append(rm.median())
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

