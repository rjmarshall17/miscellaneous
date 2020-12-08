#!/usr/bin/env python3

import os
from typing import List

"""
Amazon would like to know how much inventory exists in their closed
inventory compartments. Given a string s consisting of items as "*"
and closed compartments as an open and close "|", an array of starting
indices startIndices, and an array of ending indices endIndices, 
determine the number of items in closed compartments within the 
substring between the two indices, inclusive.

- An item is represented as an asterisk (* = ASCII decimal 42)
- A compartment is represented as a pair of pipes that may or
  may not have items between them ('|' = ASCII decimal 124).

Example

s = '|**|*|*'
startIndices = [1,1]
endIndices = [5,6]

The string has a total of 2 closed compartments, one with 2 items
and one with 1 item. For the first part of indices, (1, 5), the 
substring is '|**|*'. There are 2 items in a compartment.
For the second pair of indices, (1, 6), the substring is '|**|*|'
and there are 2 + 1 = 3 items in the compartments. 
Both of the answers are returned in an array, [2,3].

Function description

Complete the numberOfItems function in the editor below. The function
must return an integer array that contains the results for each of 
the startIndices[i] and endIndices[i] pairs.

numberOfItems has three parameters:
    s: A string to evaluate
    startIndices: An integer array, the starting indices
        The origin for indexes is 1, not 0.
    endIndices: An integer array, the ending indices
        The origin for indexes is 1, not 0.

Constraints:
    1 <= m, n <= 10**5
    1 <= startIndices[i] <= endIndices[i] <= n

Input for Custom Testing

The first line contains a string, s.
The next line contains an integer, n, the number of elements
    in startIndices
Each line i of the n subsequent lines (where 1 <= i <= n)
    contains an integer, startIndices[i]
The next line repeats the integer, n, the number of elements
    in the endIndices
Each line i of the n subsequent lines (where 1 <= i <= n)
    contains an integer, endIndices[i]

Sample Case 0
Sample Input for Custom Testing

STDIN           Function
-----           --------
*|*|        ->  s = "*|*|"
1           ->  startIndices[] size n = 1
1           ->  startIndices[i] = 1
1           ->  endIndices[] size n = 1
3           ->  endIndices[i] = 3

Sample Output

0

Explanation
s = "*|*|"
n = 1
startIndices = [1]
n = 1
endIndices = [3]

The substring from index = 1 to index = 3 is '*|*'. There are no
compartments in this substring.

"""


def count_items(items_string: str) -> int:
    # print("count_items: Got string: '%s'" % items_string)
    count = 0
    total_count = 0
    add_item = False
    for character in items_string:
        if character == '|':
            if not add_item:
                add_item = True
            total_count += count
            count = 0
            continue
        if character == '*' and add_item:
            count += 1
    return total_count


def numberOfItems(s: str, startIndices: List[int], endIndices: List[int]) -> List[int]:
    if len(startIndices) != len(endIndices):
        raise ValueError("Invalid input for start and end indices, lengths are not equal")

    counts = []
    if len(s) > 0:
        for i in range(len(startIndices)):
            counts.append(count_items(s[startIndices[i] - 1:endIndices[i]]))
    return counts


if __name__ == '__main__':
    compartments_string = input().strip()
    startIndices = []
    endIndices = []

    start_count = int(input().strip())
    for _ in range(start_count):
        startIndices.append(int(input().strip()))

    end_count = int(input().strip())
    for _ in range(end_count):
        endIndices.append(int(input().strip()))

    # print("The compartments string is: '%s', startIndices=%s endIndices=%s" % (compartments_string,
    #                                                                            startIndices,
    #                                                                            endIndices))

    expected_results = eval(open(os.environ['EXPECTED_RESULTS'],'r').read().strip())
    results = numberOfItems(s=compartments_string, startIndices=startIndices, endIndices=endIndices)
    # print("results='%s' expected_results='%s'" % (results, expected_results))
    assert results == expected_results
    print("The results from '%s':" % compartments_string)
    print("startIndices: %s" % startIndices)
    print("  endIndices: %s" % endIndices)
    print("matches the expected results: %s" % results)
