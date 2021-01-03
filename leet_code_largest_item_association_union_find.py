#!/usr/bin/env python3

import os
import sys
from typing import List
from collections import Counter

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from graphs.union_find import UnionFind


"""
In order to improve customer experience, Amazon has developed a system to provide recommendations
to the customers regarding the items they can purchase. Based on historical customer purchase
information, an item association can be defined as:

    if an item A is ordered by a customer, then item B is also likely to be ordered
    by the same customer (e.g. Book 1 in frequently ordered with Book 2).

All items that are linked together by an item association can be considered to be in the same
group. An item without any association to any other item can be considered to be in its own
item association group of size 1.

Given a list of item association relationships (i.e., group of items likely to be ordered
together), write an algorithm that output the largest item association group. If two groups
have the same number of items then select the group which contains the item that appears
first in lexicographic order.

Input

The input to the function/method consists of argument:
    itemAssociation, a list containing pairs of strings representing items that
    are ordered together.

Output

Return a list of strings representing the largest item association group, sorted
lexicographically.

Example

Input:
    itemAssociation
    [[item1, item2],
    [item3, item4],
    [item4, item5]]

Output:
    [item3, item4, item5]

Explanation:
    There are two item association groups:
    group1: [item1, item2]
    group2: [item3, item4, item5]
    In the available item associations, group2 has the largest association.
    So the output is: [item3, item4, item5]
"""


def largest_item_association(associations: List[List[str]]) -> List:
    # Start off by flattening the incoming list and sorting it
    sorted_items = sorted(set([item for sublist in associations for item in sublist]))
    # Create a mapping for the item to an ID, will be used with UnionFind
    items_to_id = {sorted_items[index]: index for index in range(len(sorted_items))}

    # Set up the union find
    uf = UnionFind(len(sorted_items))
    for items in associations:
        uf.union(items_to_id[items[0]],items_to_id[items[1]])

    # print('Items to id:\n%s' % items_to_id)
    # print(uf.union_find)
    ret = []
    # The UnionFind most_members returns the parent with the most members.
    most_members = int(uf.most_members)
    for item in sorted_items:
        if int(uf.find(items_to_id[item])) == most_members:
            ret.append(item)

    return ret


EXAMPLE_INPUT = [
    [
        ['item1', 'item2'],
        ['item3', 'item4'],
        ['item4', 'item5']
    ],
    [
        ['item1', 'item2'],
        ['item2', 'item3'],
        ['item3', 'item4'],
        ['item5', 'item6'],
        ['item6', 'item7'],
        ['item8', 'item9'],
        ['item10', 'item11'],
        ['item12', 'item13']],
]

EXPECTED_RESULTS = [
    ['item3', 'item4', 'item5'],
    ['item1', 'item2', 'item3', 'item4'],
]

if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUT):
        if i:
            print('='*80)
        print("Getting largest association for:\n%s" % input_data)
        result = largest_item_association(input_data)
        assert result == EXPECTED_RESULTS[i], \
            "The result (%s) does not match the expected result: %s" % (result,
                                                                        EXPECTED_RESULTS[i])
        print("The result (%s) matches the expected result: %s" % (result,
                                                                   EXPECTED_RESULTS[i]))
