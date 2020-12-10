#!/usr/bin/env python3

import re
from typing import List

"""
Amazon Fresh is running a promotion in which customers receive prizes for purchasing a secret combination of 
fruits. The combination will change each day, and the team running the promotion wants to use a code list to 
make it easy to change the combination. The code list contains groups of fruits. Both the order of the groups 
within the code list and the order of the fruits within the groups matter. However, between the groups of fruits,
any number, and type of fruit is allowable. The term "anything" is used to allow for any type of fruit to appear 
in that location within the group.

Consider the following secret code list: [[apple, apple], [banana, anything, banana]]

Based on the above secret code list, a customer who made either of the following purchases would win the prize:

orange, apple, apple, banana, orange, banana
apple, apple, orange, orange, banana, apple, banana, banana

Write an algorithm to output 1 if the customer is a winner else output 0.

Input:

The input to the function/method consists of two arguments:

- codeList, a list of lists of strings representing the order and grouping of specific fruits that must be 
  purchased in order to win the prize for the day.
- shoppingCart, a list of strings representing the order in which a customer purchases fruit.

Output

Return an integer 1 if the customer is a winner else return 0.

Note
'anything' in the codeList represents that any fruit can be ordered in place of 'anything' in the group.
'anything' has to be something, it cannot be "nothing."
'anything' must represent one and only one fruit.
If secret code list is empty then it is assumed that the customer is a winner.

Example 1:

Input: 
    codeList = [[apple, apple], [banana, anything, banana]] 
    shoppingCart = [orange, apple, apple, banana, orange, banana]

Output: 1

Explanation:

codeList contains two groups - [apple, apple] and [banana, anything, banana].
The second group contains 'anything' so any fruit can be ordered in place of 'anything' in the shoppingCart. 
The customer is a winner as the customer has added fruits in the order of fruits in the groups and the order 
of groups in the codeList is also maintained in the shoppingCart.

Example 2:

Input: 
    codeList = [[apple, apple], [banana, anything, banana]]
    shoppingCart = [banana, orange, banana, apple, apple]

Output: 0

Explanation:

The customer is not a winner as the customer has added the fruits in order of groups but group [banana, 
orange, banana] is not following the group [apple, apple] in the codeList.

Example 3:

Input:

    codeList = [[apple, apple], [banana, anything, banana]] 
    shoppingCart = [apple, banana, apple, banana, orange, banana]
    
Output: 0

Explanation:

The customer is not a winner as the customer has added the fruits in an order which is not following the 
order of fruit names in the first group.

Example 4:

Input:
    codeList = [[apple, apple], [apple, apple, banana]]
    shoppingCart = [apple, apple, apple, banana]
    
Output: 0

Explanation:

The customer is not a winner as the first 2 fruits form group 1, all three fruits would form group 2, but 
can't because it would contain all fruits of group 1.
"""

EXAMPLE_INPUTS = [
    {
        "codeList": [["apple", "apple"], ["banana", "anything", "banana"]],
        "shoppingCart": ["orange", "apple", "apple", "banana", "orange", "banana"],
    },
    {
        "codeList": [["apple", "apple"], ["banana", "anything", "banana"]],
        "shoppingCart": ["banana", "orange", "banana", "apple", "apple"],
    },
    {
        "codeList": [["apple", "apple"], ["banana", "anything", "banana"]],
        "shoppingCart": ["apple", "banana", "apple", "banana", "orange", "banana"],
    },
    {
        "codeList": [["apple", "apple"], ["apple", "apple", "banana"]],
        "shoppingCart": ["apple", "apple", "apple", "banana"],
    },
    {
        "codeList": [["apple", "apple"], ["banana", "anything", "banana"]],
        "shoppingCart": ["orange", "apple", "apple", "banana", "orange", "banana"],
    },
    {
        "codeList": [["apple", "apple"], ["banana", "anything", "banana"] ],
        "shoppingCart": ["apple", "apple", "orange", "orange", "banana", "apple", "banana", "banana"],
    },
    {
        "codeList": [["anything", "apple"], ["banana", "anything", "banana"] ],
        "shoppingCart": ["orange", "grapes", "apple", "orange", "orange", "banana", "apple", "banana", "banana"],
    },
    {
        "codeList": [["apple", "orange"], ["orange", "banana", "orange"]],
        "shoppingCart": ["apple", "orange", "banana", "orange", "orange", "banana", "orange", "grape"],
    },
    {
        "codeList": [["anything", "anything", "anything", "apple"], ["banana", "anything", "banana"] ],
        "shoppingCart": ["orange", "apple", "banana", "orange", "apple", "orange", "orange", "banana", "apple", "banana"],
    },
]

EXPECTED_RESULTS = [
    1,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
]


# By removing checks for spaces around the commas in the pattern, it reduced the time
# for a non-compiled search from 0.7170 to 0.6033 on average. By compiling the regular
# expression, I sped up the execution by almost 1/4 to 28.31% of the average time for
# the non-compiled search. Also make sure everything is lowercase to avoid having to
# do case specific searches.
# The time complexity for building the pattern is, at worst, O(2^m), where m is the
# size of the regular expression. Space is O(n) worst case, this would assume that
# none of the values in the code list can be replaced by a special sequence, i.e.
# \w+ for "anything".
def build_regex(code_list):
    pattern = ''
    for code_group in code_list:
        if pattern:
            pattern += r'[\w\s,]{0,}'
        pattern += ",".join([str(x).lower().replace('anything', r'\w+') for x in code_group])
    # print("code_list: %s" % code_list)
    # print("  pattern: %s" % pattern)
    return re.compile(pattern)


# There doesn't appear to be a good way to measure the time complexity of a regular
# expression search.
def fresh_promotion_check(code_list: List[List[str]], shopping_cart: List[str]) -> int:
    promotion_re = build_regex(code_list)
    # Make sure there are no spaces around the shopping cart items, it helps speed
    # up the regular expression search to not check for spaces around the commas.
    # Also make sure all of the items are in lowercase.
    # Joining all of the items from the shopping list into a string takes O(n) time,
    # where n is the length of the output string
    if promotion_re.search(','.join([x.lower().strip() for x in shopping_cart])) is None:
        return 0
    return 1


if __name__ == '__main__':
    for i, input_values in enumerate(EXAMPLE_INPUTS):
        result = fresh_promotion_check(input_values['codeList'], input_values['shoppingCart'])
        # print("The result of %d from:" % result)
        # print("    code list: %s" %  input_values['codeList'])
        # print("shopping cart: %s was correct" % input_values['shoppingCart'])
        assert result == EXPECTED_RESULTS[i]
        print("Correct result of %d from" % result)
        print("    code list: %s" % input_values['codeList'])
        print("shopping cart: %s" % input_values['shoppingCart'])
        if i < len(EXAMPLE_INPUTS) - 1:
            print("%s" % ("="*80))
