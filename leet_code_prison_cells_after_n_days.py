#!/usr/bin/env python3

from typing import List
from time import perf_counter
from copy import deepcopy

"""
957. Prison Cells After N Days

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, 
else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]

Explanation: 

The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
 

Note:

cells.length == 8
cells[i] is in {0, 1}
1 <= N <= 10^9
"""


def prison_after_n_days_brute_force(cells: List[int], n_days: int) -> List[int]:
    for i in range(n_days):
        prev = None
        for j in range(len(cells)):
            if j == 0 or j == len(cells) - 1:
                prev = cells[j]
                cells[j] = 0
            else:
                # The long version of this if is:
                # if (prev == 1 and cells[j + 1] == 1) or (prev == 0 and cells[j + 1] == 0):
                if prev == cells[j + 1]:
                    prev = cells[j]
                    cells[j] = 1
                else:
                    prev = cells[j]
                    cells[j] = 0
    return cells


def next_day(cells):
    prev = None
    for index in range(len(cells)):
        if index == 0 or index == len(cells) - 1:
            prev = cells[index]
            cells[index] = 0
        else:
            # The long version of this if is:
            # if (prev == 1 and cells[index + 1] == 1) or (prev == 0 and cells[index + 1] == 0):
            if prev == cells[index + 1]:
                prev = cells[index]
                cells[index] = 1
            else:
                prev = cells[index]
                cells[index] = 0
    return cells


def prison_after_n_days_improved(cells: List[int], n_days: int) -> List[int]:
    seen = {}
    cycle = False
    while n_days > 0:
        if not cycle:
            current_state = tuple(cells)
            if current_state in seen:
                cycle_length = seen[current_state] - n_days
                n_days %= cycle_length
                cycle = True
            else:
                seen[current_state] = n_days
        if n_days > 0:
            n_days -= 1
            cells = next_day(cells)
    return cells

EXAMPLE_INPUTS = [
    [[0, 1, 0, 1, 1, 0, 0, 1], 7],
    [[1, 0, 0, 1, 0, 0, 1, 0], 100],
    [[0, 0, 1, 0, 0, 0, 1, 0], 10000],
    [[0, 1, 0, 1, 1, 0, 0, 1], 1000000],
    [[1, 0, 0, 1, 0, 0, 1, 0], 100000000],
    [[1, 0, 0, 1, 0, 0, 1, 0], 1000000000],
]

EXPECTED_RESULTS = [
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0],
]

if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUTS):
        # Because the array of cells gets modified, we need a new copy
        brute_cells = deepcopy(input_data[0])
        improved_cells = deepcopy(input_data[0])

        # print('+'*80)
        # start_time = perf_counter()
        # result_brute = prison_after_n_days_brute_force(brute_cells, input_data[1])
        # end_time = perf_counter()
        # brute_run_time = end_time - start_time
        # print(f"Finished brute force in {brute_run_time:.8f} seconds")
        # output =  "         The results: %s\n" % result_brute
        # output += "The expected results: %s\n" %  EXPECTED_RESULTS[i]
        # output += "{} for %s and %d days" % (input_data[0], input_data[1])
        # assert result_brute == EXPECTED_RESULTS[i], output.format("does not match")
        # print(output.format("matches"))
        # print('-'*80)
        start_time = perf_counter()
        result_improved = prison_after_n_days_improved(improved_cells, input_data[1])
        end_time = perf_counter()
        improved_run_time = end_time - start_time
        print(f"   Finished improved in {improved_run_time:.8f} seconds")
        output =  "         The results: %s\n" % result_improved
        output += "The expected results: %s\n" %  EXPECTED_RESULTS[i]
        output += "{} for %s and %d days" % (input_data[0], input_data[1])
        assert result_improved == EXPECTED_RESULTS[i], output.format("does not match")
        print(output.format("matches"))
        print('-'*80)
