#!/usr/bin/env python3

from collections import deque, defaultdict
from typing import List
from pprint import pprint
# import networkx as nx
# import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use("macosx")
# from typing import List

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


EXAMPLE_INPUTS =[
    [['item1', 'item2'], ['item3', 'item4'], ['item4', 'item5']],
    [['item1', 'item2'], ['item4', 'item5'], ['item3', 'item4'], ["item1", "item4"]],
]

EXPECTED_RESULTS = [
    ['item3', 'item4', 'item5'],
    ['item1', 'item2', 'item3', 'item4', 'item5'],
]


# We build a graph and then do a breadth first search, so the time complexity is O(n) where n is
# the number of items in the input because we have to go through every item at least once.
def largest_item_association(associations: List[List[str]]):
    item_map = defaultdict(set)

    for item_pair in associations:
        item_map[item_pair[0]].add(item_pair[1])
        item_map[item_pair[1]].add(item_pair[0])

    # print("The item map is:")
    # pprint(item_map)
    # Set up the largest group and visited set.
    largest_group = []
    visited = set()

    for key, val in item_map.items():
        # print("Working on key: %s val: %s" % (key,val))
        if key not in visited:
            # print("key (%s) has not been visited" % key)
            current_group = []
            queue = deque()
            queue.append(key)           # Add the current key to the queue
            # print("Starting while queue loop")
            while queue:
                # print("The queue is: %s" % queue)
                current = queue.popleft()
                # print("current (just popped left from queue) is: %s" % current)
                # Make sure we don't visit this element again, and add it to the current
                # group.
                visited.add(current)
                current_group.append(current)
                # print("current_group: %s" % current_group)
                # If there are neighbors, then add them to the queue
                for neighbor in item_map[current]:
                    if neighbor not in visited:
                        # print("Visiting neighbor: %s" % neighbor)
                        queue.append(neighbor)
            # print("At end of while loop, checking if current group is larger")
            # If the current group is larger than the current largest_group, replace it
            if len(current_group) > len(largest_group):
                largest_group = current_group.copy()
        # else:
            # print("key %s has already been visited" % key)

    largest_group.sort()
    return largest_group


if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUTS):
        results = largest_item_association(input_data)
        assert results == EXPECTED_RESULTS[i]
        print("The results %s match the input:" % results)
        print("%s" % input_data)
