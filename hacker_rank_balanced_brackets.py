#!/usr/bin/env python3
import os

"""
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left 
of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of 
brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, 
{[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets 
encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced 
closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given  strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, 
return YES. Otherwise, return NO.

Function Description

Complete the function isBalanced in the editor below. It must return a string: YES if the sequence is balanced 
or NO if it is not.

isBalanced has the following parameter(s):

s: a string of brackets

Input Format

The first line contains a single integer n, the number of strings.
Each of the next n lines contains a single string s, a sequence of brackets.

Constraints

1 <= n <= 10**3
1 <= |s| <= 10**3 where |s| is the length of the sequence
All characters in the sequences ∈ { {, }, (, ), [, ] }.

Output Format

For each string, return YES or NO.

Sample Input

3
{[()]}
{[(])}
{{[[(())]]}}

Sample Output

YES
NO
YES

Explanation

The string {[()]} meets both criteria for being a balanced string, so we print YES on a new line.
The string {[(])} is not balanced because the brackets enclosed by the matched pair { and } are not balanced: [(]).
The string {{[[(())]]}} meets both criteria for being a balanced string, so we print YES on a new line.
"""

MATCHING_PARENTHESES = {
    '}': '{',
    ')': '(',
    ']': '[',
}


# is_balanced() will check the incoming string to see if the
# brackets are balanced.
def is_balanced(incoming_string):
    parentheses = []
    for character in incoming_string:
        if character in MATCHING_PARENTHESES.values():
            parentheses.append(character)
        elif character in MATCHING_PARENTHESES:
            if not parentheses:
                return "NO"
            if parentheses[-1] != MATCHING_PARENTHESES[character]:
                return "NO"
            parentheses.pop()
    if len(parentheses) > 0:
        return "NO"
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    expected_results = (open(os.environ['OUTPUT_PATH'].replace('output','expected_output'),'r')).read().splitlines()
    total_inputs = int(input())

    for input_counter in range(total_inputs):
        bracket_string = input()

        result = is_balanced(bracket_string)
        fptr.write(result + '\n')
        assert result == expected_results[input_counter]

    fptr.close()
    print("All tests for: %s passed" % os.environ['OUTPUT_PATH'])