#!/usr/bin/env python3

from typing import List

"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such
that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same 
element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 10*3
-10**9 <= nums[i] <= 10**9
-10**9 <= target <= 10**9
Only one valid answer exists.
"""


# The time complexity for the following should be O(n) since we
# will go through the input at most once. The space is also O(n)
# since we create a dictionary of each value.
def two_sum(nums: List[int], target: int) -> List[int]:
    remainders = {}
    for index, number in enumerate(nums):
        # print("remainders=%s" % remainders)
        # print("The current remainder for %d at index %d is: %d" % (number,
        #                                                            index,
        #                                                            target - number))
        if (target - number) in remainders:
            return [remainders[target - number], index]
        remainders[number] = index
    return []

EXAMPLE_INPUTS = [
    [[2, 7, 11, 15], 9],
    [[3, 5, -4, 8, 11, 1, -1, 6], 10],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], 17],
]

EXPECTED_RESULTS = [
    [0, 1],
    [4, 6],
    [7, 8],
]


if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUTS):
        result = two_sum(input_data[0], input_data[1])
        assert result == EXPECTED_RESULTS[i], \
            "The result (%s) does not match the expected result: %s" % (result,
                                                                        EXPECTED_RESULTS[i])
        print("The result for %s matches the expected:" % input_data)
        print("%s == %s" % (result, EXPECTED_RESULTS[i]))
