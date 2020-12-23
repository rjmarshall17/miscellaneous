#!/usr/bin/env python3

from typing import List

"""
Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

Example 1:

Input: s = "abcabc", k = 3
Output: ["abc", "bca", "cab"]

Example 2:

Input: s = "abacab", k = 3
Output: ["bac", "cab"]

Example 3:

Input: s = "awaglknagawunagwkwagl", k = 4
Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]

Explanation: 
Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", 
"nagw", "agwk", "kwag", "wagl" 
"wagl" is repeated twice, but is included in the output once.

Constraints:

The input string consists of only lowercase English letters [a-z]
0 ? k ? 26
Solution
"""


def print_numbered_array(array):
    l = len(array)
    for i in range(l):
        print(" %d " % i, end='')
    print()
    for i in range(l):
        print(" %s " % array[i], end='')
    print()
    
    
def generate_substr(string_in: str, size_k: int) -> List[str]:
    # If there is no string incoming, or the size is set to 0,
    # simply return an empty list
    if not string_in or size_k == 0:
        return []

    print_numbered_array(string_in)

    # Set up the result set which will prevent adding duplicate
    # substrings to the return value
    results = set()

    # Get the length of the string
    string_in_length = len(string_in)
    # Set up a dictionary to track seen characters to ensure that we don't
    # have substrings with duplicates.
    seen = {}
    # Set up a start value which will be the beginning of the substring we
    # are currently checking
    start = 0
    # Go through the string. The goal is to add every substring that does
    # not contain duplicate characters to the results.
    for index in range(string_in_length):
        # Check if we have a duplicate character
        if string_in[index] in seen:
            # If we do, move the start past the previous character
            print("start=%d seen['%s']=%d" % (start, string_in[index], seen[string_in[index]]))
            if start < seen[string_in[index]]:
                start = seen[string_in[index]] + 1
                print("Moving start to: %d" % start)
        # Update the last time we saw this particular character
        seen[string_in[index]] = index

        # Check if the current substring is of the size we want
        if index - start == size_k:
            # The substring would be of the correct length, add
            # it to the result set.
            results.add(string_in[start:index])
            # Bump the start index so that we will start to examine the next
            # potentially valid substring
            start += 1
    # We've exited the loop, is there a current valid substring?
    if index - start == size_k:
        results.add(string_in[start:index])
    # Convert the result set to a list and return it
    return list(results)

EXAMPLE_INPUTS = [
    ["abcabc", 3],
    ["abacab", 3],
    ["awaglknagawunagwkwagl", 4],
]

EXPECTED_RESULTS = [
    ["abc", "bca", "cab"],
    ["bac", "cab"],
    ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"],
]


if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUTS):
        if i:
            print('='*80)
        results = generate_substr(input_data[0], input_data[1])
        output = "The results (%s) {} match the expected results: %s" % (sorted(results),
                                                                         sorted(EXPECTED_RESULTS[i]))
        assert sorted(results) == sorted(EXPECTED_RESULTS[i]), output.format("did not")
        print(output.format("did"))
