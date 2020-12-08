#!/usr/bin/env python

from typing import List
from heapq import heappush, heappop, heapify

"""
Given n ropes of different lengths, we need to connect these ropes into one rope. We can connect only 2 ropes 
at a time. The cost required to connect 2 ropes is equal to sum of their lengths. The length of this connected 
rope is also equal to the sum of their lengths. This process is repeated until n ropes are connected into a 
single rope. Find the min possible cost required to connect all ropes.

Example 1:

Input: ropes = [8, 4, 6, 12]

Output: 58

Explanation: The optimal way to connect ropes is as follows
1. Connect the ropes of length 4 and 6 (cost is 10). Ropes after connecting: [8, 10, 12]
2. Connect the ropes of length 8 and 10 (cost is 18). Ropes after connecting: [18, 12]
3. Connect the ropes of length 18 and 12 (cost is 30).
Total cost to connect the ropes is 10 + 18 + 30 = 58

Example 2:

Input: ropes = [20, 4, 8, 2]

Output: 54

Example 3:

Input: ropes = [1, 2, 5, 10, 35, 89]
Output: 224

Example 4:

Input: ropes = [2, 2, 3, 3]
Output: 20

Solution

Time complexity: O(nlogn).
Space complexity: O(n).

public static int minCost(List<Integer> ropes) {
    Queue<Integer> pq = new PriorityQueue<>(ropes);
    int totalCost = 0;
    while (pq.size() > 1) {
        int cost = pq.poll() + pq.poll();
        pq.add(cost);
        totalCost += cost;
    }
    return totalCost;
}
"""

EXAMPLE_INPUTS = [
    [8, 4, 6, 12],
    [20, 4, 8, 2],
    [1, 2, 5, 10, 35, 89],
    [2, 2, 3, 3],
]

EXPECTED_RESULTS = [
    58,
    54,
    224,
    20,
]


def connect_ropes_cost(ropes: List[int]) -> int:
    total_cost = 0

    if ropes:
        if len(ropes) == 1:
            return ropes[0]
        heapify(ropes)
        while len(ropes) > 0:
            if len(ropes) > 1:
                first_cost = heappop(ropes)
                second_cost = heappop(ropes)
                total_cost += first_cost + second_cost
                if ropes:
                    heappush(ropes, first_cost + second_cost)
            else:
                total_cost += heappop(ropes)

    return total_cost


if __name__ == '__main__':
    for i, input_list in enumerate(EXAMPLE_INPUTS):
        result = connect_ropes_cost(input_list)
        # print("The result for index %d was: %d expected is: %d" % (i, result, EXPECTED_RESULTS[i]))
        assert result == EXPECTED_RESULTS[i]
        print("The cost of %d matched the expected cost for index: %d" % (result, i))
