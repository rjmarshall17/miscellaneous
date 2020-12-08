#!/usr/bin/env python3

from collections import defaultdict
from typing import List

"""
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. 
Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

Constraints:

1 <= time.length <= 6 * 104
1 <= time[i] <= 500

Approach 2 (not brute force): Hashmap

Intuition

Let's dive deep into the condition (time[i] + time[j]) % 60 == 0 to examine the relation between time[i] and time[j]. Assuming that a and b are two elements in the input array time, we have:
"""

EXAMPLE_INPUTS = [
    [30, 20, 150, 100, 40],
    [60, 60, 60],
]

EXPECTED_RESULTS = [
    3,
    3,
]


"""
Approach 1: Brute Force
One of the most straightforward approaches would be iterating through the entire array using a nested loop 
to examine that, for each element a in time, whether there is another element b such that (a + b) % 60 == 0. 
Note that this approach might be too brutal to pass an interview.
"""

# Complexity Analysis
#
# Time complexity: O(n^2) when n is the length of the input array. For each item in time, we iterate through
# the rest of the array to find a qualified complement taking O(n) time.
# Space complexity: O(1).


def brute_force_numPairsDivisibleBy60(time: List[int]) -> int:
    ret, n = 0, len(time)
    for i in range(n):
        # j starts with i+1 so that i is always to the left of j
        # to avoid repetitive counting
        for j in range(i + 1, n):
            ret += (time[i] + time[j]) % 60 == 0
    return ret


"""
Approach 2: Hashmap
Intuition

Let's dive deep into the condition (time[i] + time[j]) % 60 == 0 to examine the relation between 
time[i] and time[j]. Assuming that a and b are two elements in the input array time, we have:

(a + b) % 60 == 0
((a % 60) + (b % 60)) % 60 == 0

Therefore, either:
a % 60 == 0,
            or (a % 60) + (b % 60) == 60
b % 60 == 0,

Hence, all we need would be finding the pairs of elements in time so they meet these conditions.

Algorithm

We would iterate through the input array time and for each element a, we want to know the number 
of elements b such that:

1. b % 60 = 0, if a % 60=0
2. b % 60 = 60 - a % 60, if a % 60 <> 0

We can use Approach 1 to implement this logic by repeatedly examining the rest of time again and again
for each element a. However, we are able to improve the time complexity by consuming more space - we 
can store the frequencies of the remainder a % 60, so that we can find the number of the complements 
in O(1) time.
"""


def numPairsDivisibleBy60(time: List[int]) -> int:
    remainders = defaultdict(int)
    # print("remainders=%s" % remainders)
    ret = 0
    for t in time:
        # print("Checking time: %d %% 60 = %d" % (t, t % 60))
        if t % 60 == 0:  # check if a % 60 == 0 && b % 60 == 0
            ret += remainders[0]
            # print("in if and ret += %d remainders[0]=%s" % (remainders[0], remainders[0]))
        else:  # check if a % 60 + b % 60 == 60
            ret += remainders[60 - t % 60]
            # print("In the else, ret += %d remainders[%d]=%d" % (remainders[60 - t % 60],
            #                                                     60 - t % 60,
            #                                                     remainders[60 - t % 60]))
        remainders[t % 60] += 1  # remember to update the remainders
        # print("End of for loop, incrementing: remainders[%d] += 1 (%d)" % (t % 60, remainders[t % 60]))
    print("remainders=%s" % remainders)
    return ret


if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUTS):
        result = numPairsDivisibleBy60(time=input_data)
        assert result == EXPECTED_RESULTS[i]
        print("The result of %d for %s is correct" % (result, input_data))
