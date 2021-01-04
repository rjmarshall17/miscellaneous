#!/usr/bin/env python3

from typing import List


def print_numbered_array(array):
    l = len(array)
    for i in range(l):
        print('{:^5}'.format(str(i)), end='')
    print()
    for i in range(l):
        print('{:^5}'.format(str(array[i])), end='')
    print()
    
"""
Write a function that takes in two strings and checks if the first strings contains the
second one using the Knuth-Morris-Pratt algorithm. The function should return a boolean.
The Knuth-Morris-Pratt algorithm has a time complexity of O(n+m) where n is the length of
the string to search and m is the length of the substring for which we're searching. The
space complexity is O(m) since we need to create the pattern. 
"""

def knuth_morris_pratt(string_in, substring_in):
    # print_numbered_array(string_in)
    pattern = build_pattern(substring_in)
    # print_numbered_array(substring_in)
    # print_numbered_array(pattern)
    return does_match(string_in, substring_in, pattern)

def build_pattern(substring_in):
    pattern = [-1] * len(substring_in)
    j = 0
    i = 1
    while i < len(substring_in):
        if substring_in[i] == substring_in[j]:
            # print("build_pattern: Found match: i=%d (%s) j=%d (%s)" % (i,
            #                                                            substring_in[i],
            #                                                            j,
            #                                                            substring_in[j]))
            pattern[i] = j
            # print("build_pattern: pattern[i (%d)] = j (%d)" % (i, j))
            i += 1
            j += 1
        elif j > 0:
            # print("build_pattern: No match but j > 0, i.e. %d resetting to: pattern[j - 1] (%d) + 1 = %d" % (j,
            #                                                                                                  pattern[j-1],
            #                                                                                                  pattern[j-1]+1))
            j = pattern[j - 1] + 1
        else:
            i += 1
            # print("build_pattern: No match and j (%d) is not greater than 0 i=%d" % (j,i))
    return pattern

def does_match(string_in, substring_in, pattern):
    i = 0
    j = 0
    while i + len(substring_in) - j <= len(string_in):
        if string_in[i] == substring_in[j]:
            # print("does_match: string[i (%d)] %s == %s substring[j (%d)]" % (i,
            #                                                                  string_in[i],
            #                                                                  substring_in[j],
            #                                                                  j))
            if j == len(substring_in) - 1:
                # print("does_match: j (%d) == (%d) length of substring_in - 1" % (j,
                #                                                                  len(substring_in)-1))
                return True
            i += 1
            j += 1
            # print("does_match: incremented i=%d j=%d" % (i,j))
        elif j > 0:
            # print("does_match: No match found resetting j (%d) to pattern[j - 1 (%d)] (%d) to %d" % (j,
            #                                                                                          j-1,
            #                                                                                          pattern[j-1],
            #                                                                                          pattern[j-1]+1))
            j = pattern[j - 1] + 1
        else:
            # print("does_match: No match and j <= 0 incrementing i from %d to %d" % (i, i+1))
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