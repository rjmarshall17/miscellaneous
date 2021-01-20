#!/usr/bin/env python3

from typing import List
from time import perf_counter
from collections import defaultdict

"""
139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine 
if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]

Output: true

Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]

Output: true

Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]

Output: false

"""


def word_break_brute_force(s: str, word_dict: List[str]) -> bool:
    if len(s) == 0:
        return True

    # print("Checking word: %s" % s)
    for word in word_dict:
        if len(word) > len(s):
            continue
        if s.lower().startswith(word.lower()):
            # print("Found match for %s in: %s" % (word,s))
            result = word_break_brute_force(s[len(word):], word_dict)
            if result:
                return True
    return False


# The approach that uses the helper function seems to be the fastest for most cases
def helper(s: str, words_set: set, memo: dict) -> bool:
    if len(s) == 0:
        return True
    if s in memo:
        return memo[s]

    for word in words_set:
        if s.lower().startswith(word) and helper(s[len(word):], words_set, memo):
            memo[s] = True
            return True

    memo[s] = False
    return False


# Converting the incoming dictionary list to a set improves the search time compared with a list, i.e.
# List: x in s O(n)
# Set: x in s average: O(1) worst case O(n)
def word_break_with_helper(s: str, word_dict: List[str]) -> bool:
    words_set = set(word_dict)
    memo = {}
    return helper(s, words_set, memo)


def word_break_builtin_helper(s: str, word_dict: List[str]) -> bool:
    words_set = set(word_dict)
    memo = {}

    def get_words(s: str) -> bool:
        if len(s) == 0:
            return True
        if s in memo:
            return memo[s]

        for word in words_set:
            if s.lower().startswith(word) and get_words(s[len(word):]):
                memo[s] = True
                return True

        memo[s] = False
        return False
    return get_words(s)


# Adding the break below speeds this up significantly, also converting the word_dict to a
# set appears to speed it up a little as well, see above. This is slower than the function
# with the helper except for the last case which is much more complicated. In that case,
# this is much faster.
def word_break_dp(s: str, word_dict: List[str]) -> bool:
    dp = [True] + [False for x in range(len(s))]
    wd = set(word_dict)

    for i in range(1, len(s) + 1):
        for j in range(i - 1, -1, -1):
            if dp[j] and s[j:i] in wd:
                dp[i] = True
                break
    return dp[len(s)]


EXAMPLE_INPUT = [
    ["leetcode", ["leet", "code"]],
    ["applepenapple", ["apple", "pen"]],
    ["catsandog", ["cats", "dog", "sand", "and", "cat"]],
    ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]],
]

EXPECTED_RESULTS = [
    True,
    True,
    False,
    False
]


if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUT):
        # start_time = perf_counter()
        # result_brute = word_break_brute_force(input_data[0], input_data[1])
        # end_time = perf_counter()
        # brute_run_time = end_time - start_time

        start_time = perf_counter()
        result_helper = word_break_with_helper(input_data[0], input_data[1])
        end_time = perf_counter()
        helper_run_time = end_time - start_time

        start_time = perf_counter()
        result_dp = word_break_dp(input_data[0], input_data[1])
        end_time = perf_counter()
        dp_run_time = end_time - start_time

        start_time = perf_counter()
        result_builtin = word_break_builtin_helper(input_data[0], input_data[1])
        end_time = perf_counter()
        builtin_run_time = end_time - start_time

        # start_time = perf_counter()
        # result_start_dict = word_break_start_dict(input_data[0], input_data[1])
        # end_time = perf_counter()
        # start_dict_run_time = end_time - start_time

        output = "Result (%s) {} expected (%s) for: %s" % (result_dp,
                                                           EXPECTED_RESULTS[i],
                                                           input_data[0])
        # assert result_brute == EXPECTED_RESULTS[i], output.format("does not match")
        assert result_helper == EXPECTED_RESULTS[i], output.format("does not match")
        assert result_dp == EXPECTED_RESULTS[i], output.format("does not match")

        print(output.format("matches"))
        # print(f"Finished brute force in {brute_run_time:.8f} seconds")
        print(f"        Finished helper in {helper_run_time:.8f} seconds")
        print(f"Finished builtin helper in {helper_run_time:.8f} seconds")
        print(f"            Finished dp in {dp_run_time:.8f} seconds")

