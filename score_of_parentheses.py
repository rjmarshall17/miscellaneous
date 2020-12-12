#!/usr/bin/env python3

"""
Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:

Input: "()"
Output: 1

Example 2:

Input: "(())"
Output: 2

Example 3:

Input: "()()"
Output: 2

Example 4:

Input: "(()(()))"
Output: 6
"""


# Time: O(N) space: O(N)
def scoreOfParentheses_recursive(string_in: str) -> int:
    def Count(i, j):
        # Score of balanced () string [i:j]
        ans = bal = 0

        # Split string into primitives
        for k in range(i, j):
            bal += 1 if string_in[k] == '(' else -1

            # bal will be 0 if we have a set of balanced parentheses
            if bal == 0:
                # if k - i == 1 then we have matching parentheses
                # one after the other
                if k - i == 1:
                    # Found matching parens, add to ans
                    ans += 1
                else:
                    # The matching parens are not next to each other.
                    # Check the next substring of string_in
                    ans += 2 * Count(i + 1, k)
                # Bump i to the next index in string_in
                i = k + 1
        return ans

    # Start the recursive calls from 0 to the end of string_in
    return Count(0, len(string_in))


# Time: O(N) space O(1)
def scoreOfParentheses_iterative(string_in: str) -> int:
    ans = k = 0
    for i in range(len(string_in)):
        k += 1 if string_in[i] == "(" else -1
        if string_in[i - 1:i + 1] == "()":
            # print("Exponential 2 ** %d = %d" % (k, 2 ** k))
            ans += 2 ** k
        # print("Current value of ans: %d" % ans)
    return ans

INPUT_STRINGS = [
    "()",
    "((()))",
    "((()()()))",
]

# The below counts/results don't make sense to me, perhaps I misunderstood
# the goal of the exercise.

EXPECTED_SCORES = [
    1,
    4,
    12,
]


if __name__ == '__main__':
    for i, input in enumerate(INPUT_STRINGS):
        score_recursive = scoreOfParentheses_recursive(input)
        # print("The score for %s was: %d" % (input,score))
        assert score_recursive == EXPECTED_SCORES[i]
        print("The recursive result (%d) for %s was correct" % (score_recursive, input))
        print("="*80)
        score_iterative = scoreOfParentheses_iterative(input)
        # print("The score for %s was: %d" % (input,score))
        assert score_iterative == EXPECTED_SCORES[i]
        print("The iterative result (%d) for %s was correct" % (score_iterative, input))
        print("="*80)
