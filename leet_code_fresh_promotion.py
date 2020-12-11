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

WILDCARD = "anything"
WINNER = 1
LOSER = 0

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
    WINNER,
    LOSER,
    LOSER,
    LOSER,
    WINNER,
    WINNER,
    WINNER,
    WINNER,
    WINNER,
]


# Ran timeit to see which was faster. The non-regex version ran in an average of 1.7981394702000046
# seconds where the regex version (which has to compile the code_list every time) took an average
# of 4.25099621735003 which makes it 2.5, or so, times slower. So, the short answer is don't use
# regex, it's too slow.

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
        pattern += ",".join([str(x).lower().replace(WILDCARD, r'\w+') for x in code_group])
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
    if promotion_re.search(','.join([x.lower().strip() for x in shopping_cart])) is None:
        return LOSER
    return WINNER


# The time complexity is: O(n+m) because we will go through at most n (number of items in the
# code list) plus m (number of items in the shopping cart), space is: O(1)
def non_regex_fresh_promotion_check(code_list: List[List[str]], shopping_cart: List[str]) -> int:
    if len(code_list) > len(shopping_cart):
        return 0
    last_start = 0
    code_group = 0
    code_sublist_count = 0
    shopping_cart_index = 0

    # The code_group is for the sub-lists of the incoming code_list
    while code_group < len(code_list) and shopping_cart_index < len(shopping_cart):
        # I broke this up in order to prevent the if statement from getting so long that it
        # goes beyond the suggested line length from PEP 8 of 120 characters. This works out,
        # in essence to an or of the two conditions.
        found_match = code_list[code_group][code_sublist_count] == shopping_cart[shopping_cart_index]
        if not found_match:
            found_match = code_list[code_group][code_sublist_count] == WILDCARD
        if found_match:
            # Because we matched, either the item or against the WILDCARD, move to the next item in
            # both the current code sublist and shopping cart.
            code_sublist_count += 1
            shopping_cart_index += 1
            # If we reached the last fruit in the sublist, then move to the next sublist
            if code_sublist_count == len(code_list[code_group]):
                code_group += 1
                # last_start = shopping_cart_index
                # If we have reached the end of the code list, we're good
                if code_group == len(code_list):
                    return WINNER
                code_sublist_count = 0
        else:
            # Special case, if the code sublist count is 0, then bump the shopping cart index
            if code_sublist_count == 0:
                shopping_cart_index += 1
                last_start = shopping_cart_index
            # Else, because we didn't find a match, need to start again at the beginning of the sublist
            else:
                code_sublist_count = 0
                last_start += 1
                # Need to keep last_start up to date in case we hit this condition and need to
                # set the shopping cart index.
                shopping_cart_index = last_start
    return LOSER


if __name__ == '__main__':
    for i, input_values in enumerate(EXAMPLE_INPUTS):
        print("+"*40, i, "+"*40)
        result = non_regex_fresh_promotion_check(input_values['codeList'], input_values['shoppingCart'])
        # result = fresh_promotion_check(input_values['codeList'], input_values['shoppingCart'])
        print("The result of %d from:" % result)
        print("    code list: %s" %  input_values['codeList'])
        print("shopping cart: %s was correct" % input_values['shoppingCart'])
        assert result == EXPECTED_RESULTS[i]
        print("Correct result of %d from" % result)
        print("    code list: %s" % input_values['codeList'])
        print("shopping cart: %s" % input_values['shoppingCart'])
