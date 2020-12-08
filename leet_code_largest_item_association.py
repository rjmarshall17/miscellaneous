#!/usr/bin/env python3

from collections import deque, defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("macosx")
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

if __name__ == '__main__':
    item_association = [['item1', 'item2'], ['item3', 'item4'], ['item4', 'item5']]
    item_map = defaultdict(set)
    for item_pair in item_association:
        item_map[item_pair[0]].add(item_pair[1])
        item_map[item_pair[1]].add(item_pair[0])

    G = nx.Graph(item_map)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    plt.show()
