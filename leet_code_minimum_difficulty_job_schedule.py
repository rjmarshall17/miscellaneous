#!/usr/bin/env python3

from functools import wraps
from typing import List

"""
Leet Code 1335. Minimum Difficulty of a Job Schedule

You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the i-th 
job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum 
of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty 
of a job done in that day.

Given an array of integers jobDifficulty and an integer d. The difficulty of the i-th job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

Example 1:

Day 1: 6, 5, 4, 3, 2
Day 2: 1

Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7

Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 

Example 2:

Input: jobDifficulty = [9,9,9], d = 4
Output: -1

Explanation: If you finish a job per day you will still have a free day. you cannot find a 
schedule for the given jobs.

Example 3:

Input: jobDifficulty = [1,1,1], d = 3
Output: 3

Explanation: The schedule is one job per day. total difficulty will be 3.

Example 4:

Input: jobDifficulty = [7,1,7,1,7,1], d = 3
Output: 15
Example 5:

Input: jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
Output: 843
 

Constraints:

1 <= jobDifficulty.length <= 300
0 <= jobDifficulty[i] <= 1000
1 <= d <= 10
"""


def memoize(func):
    memo = {}
    @wraps(func)
    def inner(*args):
        if (args,) not in memo:
            memo[(args,)] = func(*args)
        # print("%s returning: %s args: %s" % (func.__name__, memo[(args,)], (*args,)))
        return memo[(args,)]
    return inner


def minimum_difficulty(job_difficulty: List[int], days: int) -> int:
    # First check if the number of jobs is less than the available number of
    # days, in which case it is not possible to schedule the jobs.
    if len(job_difficulty) < days:
        return -1

    # Next check if the number of jobs is equal to the number of days,
    # in which case the job difficulty will be the some of the job
    # difficulties.
    if len(job_difficulty) == days:
        return sum(job_difficulty)

    @memoize
    def array_max(start: int, end: int):
        return max(job_difficulty[start:end])

    @memoize
    def recursion(prev: int, day: int) -> int:
        # if we come to the last day, we need to do all the follwing jobs
        if day == 1:
            return array_max(prev, len(job_difficulty))
        # else we check all the possibilities
        difficulty = float('inf')
        # we could stop at job[i] for current day, where i is any job greater than prev index
        # but less than len(jobDifficulty) - day + 2
        for i in range(prev + 1, len(job_difficulty) - day + 2):
            cur = array_max(prev, i) + recursion(i, day - 1)
            difficulty = min(cur, difficulty)
        # we return the min difficulty after current day
        return difficulty

    res = recursion(0, days)
    if res == float('inf'):
        return -1
    else:
        return res


EXAMPLE_INPUT = [
    [[6, 5, 4, 3, 2, 1], 2],
    [[9, 9, 9], 4],
    [[1, 1, 1], 3],
    [[7, 1, 7, 1, 7, 1], 3],
    [[11, 111, 22, 222, 33, 333, 44, 444], 6],
]


EXPECTED_RESULTS = [
    7,
    -1,
    3,
    15,
    843,
]


if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUT):
        result = minimum_difficulty(input_data[0], input_data[1])
        print("The result for %s is: %d expected: %d" % (input_data,
                                                         result,
                                                         EXPECTED_RESULTS[i]))
