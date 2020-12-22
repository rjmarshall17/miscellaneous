#!/usr/bin/env python3

from typing import List

"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3

Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1

Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3

Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

# The time complexity of this function is O(n) where n is the length
# of the incoming string. The space complexity is O(min(n,a)) where
# n is the length of the incoming string and a is the list of unique
# characters in the string. This is because the last_seen dictionary
# will have a size of a.
def length_of_longest_substring(string_in: str) -> int:
    if len(string_in) == 0:
        return '', 0
    start_index = 0
    last_seen = {}
    longest = [0,1]
    # Loop through the incoming string one character at a time
    for string_index, current_char in enumerate(string_in):
        # print("i=%d longest=%s" % (i,longest))
        if current_char in last_seen:
            start_index = max(start_index, last_seen[current_char] + 1)
            # print("start=%d" % start)
        # print("longest[1] (%d) - longest[0] (%d) = %d i (%d) + 1 - start(%d) = %d" % (longest[1],longest[0], longest[1]-longest[0],i,start,i+1-start))
        if longest[1] - longest[0] < string_index + 1 - start_index:
            longest = [start_index, string_index + 1]
        last_seen[current_char] = string_index
    return string_in[longest[0]:longest[1]], longest[1] - longest[0]


EXAMPLE_INPUTS = [
    'abcabcbb',
    'bbbbb',
    'pwwkew',
    '',
    'clementisacap',
]

EXPECTED_RESULTS = [
    3,
    1,
    3,
    0,
    8,
]
if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUTS):
        results = length_of_longest_substring(input_data)
        assert results[1] == EXPECTED_RESULTS[i], \
            "The result (%d - %s) for %s did not match the expected result: %d" % (results[1],
                                                                                   results[0],
                                                                                   input_data,
                                                                                   EXPECTED_RESULTS[i])
        print("The result (%d - %s) for %s matched the expected result: %d" % (results[1],
                                                                               results[0],
                                                                               input_data,
                                                                               EXPECTED_RESULTS[i]))