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
All characters in the sequences ? { {, }, (, ), [, ] }.

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

======================================
Balanced Brackets Challenge O(1) Space

In order to do an O(1) space, you can?t use a stack and you need to use a pointer instead. That means that
you have a pointer which ?acts? like a stack. 

Start checking the characters in the string.
If the current character is an open bracket, stack pointer must be incremented to point to that character

If the current character is a close bracket, is the character at the stack pointer the corresponding open 
bracket? If no, return False

If yes, then change the current character, and the character at the stack pointer, to a fill character, move 
the stack pointer back to the closest open bracket.

Using the following string:

0 1 2 3 4 5 6 7 8 9
{ } [ ] { [ ( ) ] }

Initial value of stack pointer is -1.
Start through the string with index at 0. 
We find an open bracket, move stack pointer to 0
Check character at index 1
This is a close bracket, check if stack pointer > 0, if no, then we have a mismatch, return False. Else, 
if yes, is the character at stack pointer index the opening bracket that matches our current closing bracket?
Then replace each character with ?#?, i.e.:

0 1 2 3 4 5 6 7 8 9
# # [ ] { [ ( ) ] }

Decrement the stack pointer, it would go to -1, do this in a while loop that exits when either: The current 
character is not a fill character or the stack pointer is < 0

Continue checking the string. The character at index 2 is an open bracket, since the stack pointer is < 0, 
move it to index 2.
Continue checking the string at index 3. 
This is a closing bracket, check if stack pointer > 0, if yes and character at the stack pointer is the 
corresponding open bracket, set both to fill character, i.e.:

0 1 2 3 4 5 6 7 8 9
# # # # { [ ( ) ] }

Loop to decrement the stack pointer again.

Continue checking string at index 4, it?s an open bracket and the stack pointer is < 0, move stack pointer to 4. 
Check character at index 5, it?s an open bracket move stack pointer to 5. Check character at index 6, it?s an 
open bracket move stack pointer to 6.
Check character at index 7, it?s a close bracket: Does this match the open bracket at stack pointer (index 6), 
yes, so replace current character and character under stack pointer to fill character ,i.e.:

0 1 2 3 4 5 6 7 8 9
# # # # { [ # # ] }

move stack pointer back to the next open, i.e. non-fill character, index in string, i.e.5
Check character at index 8. It?s a closing bracket, check the character at the stack pointer, does it match? 
Yes, replace both with fill character, i.e.:

0 1 2 3 4 5 6 7 8 9
# # # # { # # # # }

Decrement stack pointer to open bracket, i.e. 4
Continue checking character at index 9. It?s a close bracket, replace the brackets will fill characters, i.e.:

0 1 2 3 4 5 6 7 8 9
# # # # # # # # # #

Decrement the stack pointer, it will end up at -1

If we finish the string, and the stack pointer is at -1, we must have found all of the matches, return True. If the stack pointer is NOT at -1, then we still have open brackets return False.
"""


def print_numbered_array(array):
    l = len(array)
    for i in range(l):
        print('{:^5}'.format(str(i)), end='')
    print()
    for i in range(l):
        print('{:^5}'.format(str(array[i])), end='')
    print()


def is_balanced(string):
    check_string = [x for x in string]
    FILL_CHARACTER = '#'
    BRACKETS = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    stack = -1
    for index in range(len(check_string)):
        # print_numbered_array(check_string)
        # print("Current index=%d stack=%d" % (index, stack))
        if check_string[index] in BRACKETS.values():
            stack = index
        elif check_string[index] in BRACKETS:
            if stack < 0:
                return False
            # print("Checking character at stack=%d %s index=%d %s which is the closing bracket for: %s" %
            #       (stack,
            #        check_string[stack],
            #        index,
            #        check_string[index],
            #        BRACKETS[check_string[index]]
            #        ))
            if check_string[stack] == BRACKETS[check_string[index]]:
                check_string[stack] = FILL_CHARACTER
                check_string[index] = FILL_CHARACTER
            else:
                return False
            while check_string[stack] == FILL_CHARACTER:
                stack -= 1
                # print("In while stack=%d" % stack)
                if stack < 0:
                    break
        else:
            return False

    # print_numbered_array(check_string)
    # print("At end index=%d stack=%d" % (index, stack))
    return stack == -1


EXAMPLE_INPUTS = [
    '{}[]{[()]}',           # 0
    '}',                    # 1
    '}][}}(}][))]',         # 2
    '[](){()}',             # 3
    '()',                   # 4
    '({}([][]))[]()',       # 5
    '{)[](}]}]}))}(())(',   # 6
    '([[)',                 # 7
    '{}',                   # 8
    '}([[{)[]))]{){}[',     # 9
    '{]]{()}{])',           # 10
    '(){}',                 # 11
    '{}{()}{{}}',           # 12
]

EXPECTED_RESULTS = [
    True,                   # 0
    False,                  # 1
    False,                  # 2
    True,                   # 3
    True,                   # 4
    True,                   # 5
    False,                  # 6
    False,                  # 7
    True,                   # 8
    False,                  # 9
    False,                  # 10
    True,                   # 11
    True,                   # 12
]


if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUTS):
        result = is_balanced(input_data)
        assert result is EXPECTED_RESULTS[i], \
            "Result %s does not match expected results %s for: %s" % (result,
                                                                      EXPECTED_RESULTS[i],
                                                                      input_data)
        print("The result is %5s for: %s" % (result, input_data))


