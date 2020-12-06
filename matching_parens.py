#!/usr/bin/env python3

import sys

MATCHING_PARENTHESES = {
    '}': '{',
    ')': '(',
    ']': '[',
}


# This is apparently O(N^2) time complexity but O(N) for space
def matchingParentheses(string_in):
    parentheses = []
    for character in string_in:
        if character in MATCHING_PARENTHESES.values():
            parentheses.append(character)
        elif character in MATCHING_PARENTHESES:
            # In case we start off with a closed parentheses and there
            # is nothing in the stack
            if not parentheses:
                return False
            if parentheses[-1] != MATCHING_PARENTHESES[character]:
                return False
            parentheses.pop()
    if len(parentheses) > 0:
        return False
    return True


if __name__ == '__main__':
    if matchingParentheses(sys.argv[1]):
        print("The parentheses all matched in: %s" % sys.argv[1])
    else:
        print("There were mismatched parentheses in: %s" % (sys.argv[1]))