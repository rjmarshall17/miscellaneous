#!/usr/bin/env python3

import os
from typing import List
from timeit import default_timer as timer

"""
Amazon would like to know how much inventory exists in their closed
inventory compartments. Given a string s consisting of items as "*"
and closed compartments as an open and close "|", an array of starting
indices start_indices, and an array of ending indices end_indices, 
determine the number of items in closed compartments within the 
substring between the two indices, inclusive.

- An item is represented as an asterisk (* = ASCII decimal 42)
- A compartment is represented as a pair of pipes that may or
  may not have items between them ('|' = ASCII decimal 124).

Example

s = '|**|*|*'
start_indices = [1,1]
end_indices = [5,6]

The string has a total of 2 closed compartments, one with 2 items
and one with 1 item. For the first part of indices, (1, 5), the 
substring is '|**|*'. There are 2 items in a compartment.
For the second pair of indices, (1, 6), the substring is '|**|*|'
and there are 2 + 1 = 3 items in the compartments. 
Both of the answers are returned in an array, [2,3].

Function description

Complete the numberOfItems function in the editor below. The function
must return an integer array that contains the results for each of 
the start_indices[i] and end_indices[i] pairs.

numberOfItems has three parameters:
    s: A string to evaluate
    start_indices: An integer array, the starting indices
        The origin for indexes is 1, not 0.
    end_indices: An integer array, the ending indices
        The origin for indexes is 1, not 0.

Constraints:
    1 <= m, n <= 10**5
    1 <= start_indices[i] <= end_indices[i] <= n

Input for Custom Testing

The first line contains a string, s.
The next line contains an integer, n, the number of elements
    in start_indices
Each line i of the n subsequent lines (where 1 <= i <= n)
    contains an integer, start_indices[i]
The next line repeats the integer, n, the number of elements
    in the end_indices
Each line i of the n subsequent lines (where 1 <= i <= n)
    contains an integer, end_indices[i]

Sample Case 0
Sample Input for Custom Testing

STDIN           Function
-----           --------
*|*|        ->  s = "*|*|"
1           ->  start_indices[] size n = 1
1           ->  start_indices[i] = 1
1           ->  end_indices[] size n = 1
3           ->  end_indices[i] = 3

Sample Output

0

Explanation
s = "*|*|"
n = 1
start_indices = [1]
n = 1
end_indices = [3]

The substring from index = 1 to index = 3 is '*|*'. There are no
compartments in this substring.

"""


def count_items(items_string: str) -> int:
    # print("count_items: Got string: '%s'" % items_string)
    # If we don't have at least one compartment, return 0
    if items_string.count('|') < 2:
        return 0
    count = 0
    total_count = 0
    add_item = False
    # Time complexity: O(n) where n = length of the string,
    # Space complexity: O(1)
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


def rfind_count_items(items_string: str) -> int:
    if items_string.count('|') < 2:
        return 0
    return items_string[items_string.find('|'):items_string.rfind('|')].count('*')


# Time complexity: O(mn) where m is the number of indices and n is the number of elements
# Space complexity: O(1)
def numberOfItems(compartment_string: str, start_indices: List[int], end_indices: List[int]) -> List[int]:
    if len(start_indices) != len(end_indices):
        raise ValueError("Invalid input for start and end indices, lengths are not equal")

    counts = []
    if compartment_string:
        for i in range(len(start_indices)):
            counts.append(count_items(compartment_string[start_indices[i] - 1:end_indices[i]]))
    return counts


def rfind_numberOfItems(compartment_string: str, start_indices: List[int], end_indices: List[int]) -> List[int]:
    if len(start_indices) != len(end_indices):
        raise ValueError("Invalid input for start and end indices, lengths are not equal")

    counts = []
    if compartment_string:
        for i in range(len(start_indices)):
            counts.append(rfind_count_items(compartment_string[start_indices[i] - 1:end_indices[i]]))
    return counts


if __name__ == '__main__':
    compartments_string = input().strip()
    start_indices = []
    end_indices = []

    start_count = int(input().strip())
    for _ in range(start_count):
        start_indices.append(int(input().strip()))

    end_count = int(input().strip())
    for _ in range(end_count):
        end_indices.append(int(input().strip()))

    # print("The compartments string is: '%s', start_indices=%s end_indices=%s" % (compartments_string,
    #                                                                            start_indices,
    #                                                                            end_indices))

    expected_results = eval(open(os.environ['EXPECTED_RESULTS'],'r').read().strip())
    results_start_time = timer()
    results = numberOfItems(compartment_string=compartments_string,
                            start_indices=start_indices,
                            end_indices=end_indices)
    elapsed_time = timer() - results_start_time
    print("      The elapsed time was: %.10f" % elapsed_time)
    rfind_results_start_time = timer()
    rfind_results = rfind_numberOfItems(compartment_string=compartments_string,
                                        start_indices=start_indices,
                                        end_indices=end_indices)
    rfind_elapsed_time = timer() - rfind_results_start_time
    print("The rfind elapsed time was: %.10f" % rfind_elapsed_time)
    # print("results='%s' expected_results='%s'" % (results, expected_results))
    assert results == expected_results, "The results did not match the expected results"
    print("The results matched the expected results")
    # print("The results from '%s':" % compartments_string)
    # print("start_indices: %s" % start_indices)
    # print("  end_indices: %s" % end_indices)
    # print("matches the expected results: %s" % results)
    assert rfind_results == expected_results, "The rfind results did not match the expected results"
    print("The rfind results matched the expected results")
