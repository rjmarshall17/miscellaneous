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

def get_number(list_node: ListNode) -> int:
    number = ''
    current = list_node
    while current is not None:
        number += str(current.val)
        current = current.next
    number = number[::-1]
    # print("get_number returning: %d" % int(number))
    return int(number)

def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    number1 = get_number(l1)
    number2 = get_number(l2)
    # print("Number1=%d number2=%d" % (number1, number2))
    total = number1 + number2
    current = None
    for number in str(total)[::-1]:
        if current is None:
            current = ListNode(int(number))
            return_list = current
        else:
            ln = ListNode(int(number))
            current.next = ln
            current = current.next
            
    # print("Add two numbers returning: %s" % return_list)
    return return_list

def build_list_node(nums: List[int]) -> ListNode:
    current = None
    return_ln = None
    for number in reversed(nums):
        if current is None:
            current = ListNode(number)
            return_ln = current
        else:
            ln = ListNode(number)
            current.next = ln
            current = current.next
    return return_ln

EXAMPLE_INPUTS = [
    [build_list_node([3, 4, 2]),
     build_list_node([4, 6, 5])],
    [build_list_node([0]),
     build_list_node([0])],
    [build_list_node([9]*7),
     build_list_node([9]*4)]
]

EXPECTED_RESULTS = [
    build_list_node([8,0,7]),
    build_list_node([0]),
    build_list_node([1, 0, 0, 0, 9, 9, 9, 8]),
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

