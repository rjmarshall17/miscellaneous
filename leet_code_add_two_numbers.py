#!/usr/bin/env python3

from typing import List

"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits 
are stored in reverse order, and each of their nodes contains a single digit. Add the two 
numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

2->4->3
5->6->4

8->0->7

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]

Explanation: 342 + 465 = 807.

Example 2:

0
0

0

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        current = self
        output = ''
        while current:
            if len(output) > 0:
                output += '->'
            output += str(current.val)
            current = current.next
        return output

    def __eq__(self, other):
        c1 = self
        c2 = other
        while c1 is not None:
            if c1.val != c2.val:
                return False
            c1 = c1.next
            c2 = c2.next
            if c2 is None:
                if c1 is not None:
                    return False
        if c2 is not None:
            return False
        return True


# The time complexity for this is O(n) because we need to
# go through the entire linked list.
def get_number(list_node: ListNode) -> int:
    number = ''
    current = list_node
    while current is not None:
        number += str(current.val)
        current = current.next
    number = number[::-1]
    # print("get_number returning: %d" % int(number))
    return int(number)


# The time complexity here is O(a+b+c) because we have three linked lists
# that all need to be either read or created. The conversion of the integer
# to a string is an O(n) operation as well with space being O(n)
def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    number1 = get_number(l1)
    number2 = get_number(l2)
    # print("Number1=%d number2=%d" % (number1, number2))
    total = number1 + number2
    current = None
    return build_list_node([int(x) for x in str(total)])


# This is an O(n) operation and O(n) for space as well.
def build_list_node(nums: List[int]) -> ListNode:
    current = None
    return_ln = None
    for number in nums[::-1]:
        if current is None:
            current = ListNode(number)
            return_ln = current
        else:
            ln = ListNode(number)
            current.next = ln
            current = current.next
    return return_ln


EXAMPLE_INPUTS = [
    [build_list_node([int(x) for x in str(342)]),
     build_list_node([int(x) for x in str(465)])],
    [build_list_node([0]),
     build_list_node([0])],
    [build_list_node([9]*7),
     build_list_node([9]*4)]
]

EXPECTED_RESULTS = [
    build_list_node([int(x) for x in str(807)]),
    build_list_node([0]),
    build_list_node([int(x) for x in str(10009998)]),
]


if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUTS):
        # print("l1 is: %s" % input_data[0])
        # print("l2 is: %s" % input_data[1])
        result = add_two_numbers(input_data[0], input_data[1])
        assert result == EXPECTED_RESULTS[i], \
            "The result %s does not match the expected result: %s" % (result,
                                                                      EXPECTED_RESULTS[i])
        print("Result %s matched expected result: %s" % (result,
                                                         EXPECTED_RESULTS[i]))

