#!/usr/bin/env python3

import os

"""
Amazon would like to know how much inventory exists in their closed
inventory compartments. Given a string s consisting of items as "*"
and closed compartments as an open and close "|", an array of starting
indices startIndices, and an array of ending indices endIndices, 
determine the number of items in closed compartments within the 
substring between the two indices, inclusive.

- An item is represented as an asterisk (* = ASCII decimal 42)
- A compartment is represented as a pair of pipes that may or
  may not have items between them ('|' = ASCII decimal 124).

Example

s = '|**|*|*'
startIndices = [1,1]
endIndices = [5,6]

The string has a total of 2 closed compartments, one with 2 items
and one with 1 item. For the first part of indices, (1, 5), the 
substring is '|**|*'. There are 2 items in a compartment.
For the second pair of indices, (1, 6), the substring is '|**|*|'
and there are 2 + 1 = 3 items in the compartments. 
Both of the answers are returned in an array, [2,3].

Function description

Complete the numberOfItems function in the editor below. The function
must return an integer array that contains the results for each of 
the startIndices[i] and endIndices[i] pairs.

numberOfItems has three parameters:
    s: A string to evaluate
    startIndices: An integer array, the starting indices
        The origin for indexes is 1, not 0.
    endIndices: An integer array, the ending indices
        The origin for indexes is 1, not 0.

Constraints:
    1 <= m, n <= 10**5
    1 <= startIndices[i] <= endIndices[i] <= n

Input for Custom Testing

The first line contains a string, s.
The next line contains an integer, n, the number of elements
    in startIndices
Each line i of the n subsequent lines (where 1 <= i <= n)
    contains an integer, startIndices[i]
The next line repeats the integer, n, the number of elements
    in the endIndices
Each line i of the n subsequent lines (where 1 <= i <= n)
    contains an integer, endIndices[i]

Sample Case 0
Sample Input for Custom Testing

STDIN           Function
-----           --------
*|*|        ->  s = "*|*|"
1           ->  startIndices[] size n = 1
1           ->  startIndices[i] = 1
1           ->  endIndices[] size n = 1
3           ->  endIndices[i] = 3

Sample Output

0

Explanation
s = "*|*|"
n = 1
startIndices = [1]
n = 1
endIndices = [3]

The substring from index = 1 to index = 3 is '*|*'. There are no
compartments in this substring.

"""
