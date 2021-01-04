#!/usr/bin/env python3

from typing import List

"""
Write a function that takes in two strings and checks if the first strings contains the
second one using the Knuth-Morris-Pratt algorithm. The function should return a boolean
"""

def knuth_morris_pratt(string_in, substring_in):
    pattern = build_pattern(substring_in)
    return does_match(string_in, substring_in, pattern)

def build_pattern(substring_in):
    pattern = [-1] * len(substring_in)
    j = 0
    i = 1
    while i < len(substring_in):
        if substring_in[i] == substring_in[j]:
            pattern[i] = j
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return pattern

def does_match(string_in, substring_in, pattern):
    i = 0
    j = 0
    while i + len(substring_in) - j <= len(string_in):
        if string_in[i] == substring_in[j]:
            if j == len(substring_in) - 1:
                return True
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return False

EXAMPLE_INPUTS = [
    ["aefoaefcdaefcdaed", "aefcdaed"],
    ["testwafwafawfawfawfawfawfawfawfa", "fawfawfawfawfa"],
    ["tesseatesgawatewtesaffawgfawtteafawtesftawfawfawfwfawftest", "test"],
    ["aaabaabacdedfaabaabaaa", "aabaabaaa"],
    ["abxabcabcaby", "abcaby"],
    ["decadaafcdf", "daf"],
]

EXPECTED_RESULTS = [
    True,
    True,
    True,
    True,
    True,
    False,
]

if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUTS):
        result = knuth_morris_pratt(input_data[0], input_data[1])
        assert result is EXPECTED_RESULTS[i], \
            "The result for %s and %s of %s does not match expected result: %s" % (
                input_data[0],
                input_data[1],
                result,
                EXPECTED_RESULTS[i]
            )
        print("Correct result of %5s for %s and %s" % (result,
                                                      input_data[0],
                                                      input_data[1]))