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
    # Starting with the incoming string and an integer value that will determine
    # the size of the strings to return. We will need to loop through the string,
    # check if we've seen this character before. If we have we will need to update
    # the start of substring value to just pass the last time we saw this character.
    # We need to be sure that we don't move the start backwards, so only move it
    # past the last time, plus 1, that we saw a character if it is less or equal
    # to the last time we saw that character.
    # If we have found a substring of the correct length, then add it to the result
    # and move the start pointer over 1.
    results = set()
    seen = {}
    start = 0
    string_in_len = len(string_in)
    for i in range(string_in_len):
        if string_in[i] in seen:
            if start <= seen[string_in[i]]:
                start = seen[string_in[i]] + 1
        seen[string_in[i]] = i
        if (i + 1) - start == size_k:
            results.add(string_in[start:i + 1])
            start += 1
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
        error_output = "The results (%s) did not match the expected results: %s" %\
                       (sorted(results),sorted(EXPECTED_RESULTS[i]))
        assert sorted(results) == sorted(EXPECTED_RESULTS[i]), error_output
        print("The results matched the expected results:")
        print('%s' % sorted(results))
        print('%s' % sorted(EXPECTED_RESULTS[i]))
