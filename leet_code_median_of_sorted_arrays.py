#!/usr/bin/env python3

from typing import List

"""
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median 
of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000

Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000

Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10**6 <= nums1[i], nums2[i] <= 10**6
"""


# The time complexity of this function is O(NlogN) because we need to
# combine the lists. The combination of the two lists is O(N+M) where
# N and M are the respective lengths of the two lists.
def median_of_arrays(array1: List[int], array2: List[int]) -> float:
    # The sort of the two arrays in O(NlogN)
    both_arrays = sorted(array1 + array2)
    if len(both_arrays) == 1:
        return both_arrays[0]
    if len(both_arrays) % 2 == 0:
        if len(both_arrays) == 2:
            return sum(both_arrays) / 2
        index = (len(both_arrays) - 1) // 2
        return (both_arrays[index] + both_arrays[index+1]) / 2
    else:
        return both_arrays[len(both_arrays) // 2]


EXAMPLE_INPUTS = [
    [[1, 3], [2]],
    [[1,2], [3, 4]],
    [[0,0], [0, 0]],
    [[], [1]],
    [[2], []],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [20, 21, 22]],
]

EXPECTED_RESULTS = [
    2.0,
    2.5,
    0,
    1.0,
    2.0,
    6.5,
]


if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUTS):
        result = median_of_arrays(input_data[0], input_data[1])
        output = "The result (%.6f) for %s {} match the expected result: %.6f" % (result,
                                                                                  input_data,
                                                                                  EXPECTED_RESULTS[i])
        assert result == EXPECTED_RESULTS[i], output.format('does not')
        print(output.format('does'))


