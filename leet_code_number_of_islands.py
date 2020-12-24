#!/usr/bin/env python3

from typing import List
from collections import deque

"""
200. Number of Islands

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or 
vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

Output: 3

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

CHECK_DIRECTIONS = [
    (1, 0),             # Up
    (-1, 0),            # Down
    (0, 1),             # Right
    (0, -1),            # Left
]

def print_grid(grid: List[List[str]]):
    for row in grid:
        print(row)


def number_of_islands_iterative(grid: List[List[str]]) -> int:
    number_of_islands = 0
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1':
                number_of_islands += 1
                # print("{0} number of islands: {1} {0}".format('-'*30,number_of_islands))
                replace_with_water_iterative(grid, rows, cols, row, col)
    return number_of_islands

def replace_with_water_iterative(grid: List[List[str]], rows: int, cols: int, row: int, col: int):
    # Set up a queue to track land we find while checking around the incoming
    # row/col.
    # print("The incoming grid:")
    # print_grid(grid)
    queue = deque()
    # Add the incoming values to the queue
    queue.append((row, col))
    # Replace the land with water at that position
    grid[row][col] = '0'
    while queue:
        # Grab the row and col from the queue
        row, col = queue.popleft()
        # We set up CHECK_DIRECTIONS to make it easier to go through the four
        # directions, up, down, left and right, that we need to check for more
        # land for this current island.
        for direction in CHECK_DIRECTIONS:
            check_row = row + direction[0]
            check_col = col + direction[1]
            if ((check_row > -1 and check_row < rows) and
                    (check_col > -1 and check_col < cols) and
                    (grid[check_row][check_col] == '1')):
                # If the current check_row and check_col are in the grid and are
                # land, then we need to add this location to the queue and set it
                # to water, i.e. '0'
                queue.append((check_row, check_col))
                grid[check_row][check_col] = '0'
    # print("The current grid:")
    # print_grid(grid)
        

EXAMPLE_INPUTS = [
    [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ],
    [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ],
    [
        ["1", "1", "1", "0", "0", "0", "0", "1", "1"],
        ["1", "1", "1", "0", "0", "1", "0", "1", "1"],
        ["1", "0", "1", "0", "0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "1", "1", "0", "0", "0", "0", "0"],
        ["0", "0", "1", "1", "0", "1", "1", "0", "0"],
        ["0", "0", "0", "1", "0", "0", "0", "1", "1"],
        ["0", "0", "0", "1", "0", "0", "0", "1", "1"],
    ],
]

EXPECTED_RESULTS = [
    1,
    3,
    8,
]


if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUTS):
        # if i:
        #     print("="*80)
        result = number_of_islands_iterative(input_data)
        output = "The result (%d) {} match the expected result: %d" % (result,
                                                                       EXPECTED_RESULTS[i])
        assert result == EXPECTED_RESULTS[i], output.format("did not")
        print(output.format("did"))
