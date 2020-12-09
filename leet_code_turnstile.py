#!/usr/bin/env python3

from typing import List
from collections import deque

"""
A university has exactly one turnstile. It can be used either as an exit or an entrance. Unfortunately,
sometimes many people want to pass through the turnstile and their directions can be different. The
i-th person comes to the turnstile at time[i] and wants to either exit the university if direction[i] == 1 
or enter the university if direction[i] == 0. People form two queues, one to exit and one to enter.
They are ordered by the time when they came to the turnstile and, if the times are equal, by their indices.

If some person wants to enter the university and another person wants to leave the university at the
same moment there are three cases:

-   If in the previous second the turnstile was not used (maybe it was used before, but not at the 
    previous second), then the person who wants to leave goes first.
-   If in the previous second the turnstile was used as an exit, then the person who wants to leave goes first.
-   If in the previous second the turnstile was used as an entrance, then the person who wants to
    enter goes first.

Passing through the turnstile takes 1 second.

For each person find the time when they will pass through the turnstile.

Function Description:

    Complete the function getTimes in the editor below.
    
    getTimes has the following parameters:
    
    int time[n]: an array of n integers where the value at index i is the time in seconds
    when the i-th person will come to the turnstile
    
    int direction[n]: an array of integers where the value at index i is the direction of 
    the i-th person
    
    returns:
    
    int[n]: an array of n integers where the value at index i is the time when the i-th person
    will pass the turnstile.
    
Constraints:

1 <= n <= 10**5
0 <= time[i] <= 10**9 for 0 <= i <= n-1
time[i] <= time[i + 1] for 0 <= i <= n-2
0 <= direction[i] <= 1 for 0 <= i <= n-1

Sample Input 0:

STDIN           Function
-----           --------
4           ->  time[] size n = 4
0           ->  time = [0, 0, 1, 5]
0
1
5
4           ->  direction[] size n = 4
0           ->  direction = [0, 1, 1, 0]
1
1
0

Sample Output 0:
2
0
1
5

Explanation:

The first person arrives at 0 seconds, but his/her direction (direction = 0) is to enter the university
so, because the turnstile wasn't in use, the person exiting (direction = 1), i.e. person 2 (0 in the output) 
goes first. It takes 1 second to exit, at which point person 3 arrives who also wants to exit, so person
3 goes first. No one else arrives until 5 seconds, so the first person is allowed to enter (direction = 0)
the university so his/her time is 2 (had to wait for two people at 1 second each to exit). The final person
arrives at 5 seconds and can immediately enter the university.
"""

EXAMPLE_INPUTS = [
    [[0, 0, 1, 5], [0, 1, 1, 0]],
    [[1, 2, 4], [0, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 3, 3, 4, 5, 6, 7, 7], [1, 1, 0, 0, 0, 1, 1, 1, 1]],
]

EXPECTED_RESULTS = [
    [2, 0, 1, 5],
    [1, 2, 4],
    [1, 2],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
]


EXITING = 1
ENTERING = 0
ENETERING_EXITING = ["Entering", "Exiting"]


def let_person_go(person1, person2, the_queue, return_times):
    return_times[person1[2]] = person1[0]
    person2[0] += 1
    # print("About the prepend person2: %s" % person2)
    # The appendleft() is O(1) for time complexity
    the_queue.appendleft(person2)
    # print("The queue is now: %s" % the_queue)


def turnstile(times: List[int], directions: List[int]) -> List[int]:
    # The queue is setup using the incoming times and directions along
    # with the index of the element.
    # Creating the initial queue is going to take O(n) where n is the
    # number of times/directions, space is also O(n)
    the_queue = deque([[times[i],directions[i], i] for i in range(len(times))])
    # print("The queue is:\n%s" % the_queue)

    # Set up the return times array
    return_times = [-1] * len(times)

    # Set the last direction to exit since we prefer exit if the turnstile has not
    # been used, and set last_used to -1 to indicate we haven't used it yet
    last_direction = 1
    last_used = -1

    # breakpoint()
    while the_queue:
        # Because this is a deque, a pop/popleft is O(1) time.
        current = the_queue.popleft()
        # print("The current is: %s last used was: %d" % (current, last_used))
        if current[0] <= last_used:
            current[0] = last_used + 1
        # If the current person arrived at the same time as the next person
        # in the queue, decide who goes first by direction
        if the_queue and current[0] == the_queue[0][0]:
            next_person = the_queue.popleft()
            # print("The current person is: %s the next person is: %s" % (current,
            #                                                             next_person))
            # Check to see if the turnstile has just been used, or if
            # it hasn't been used for at least 1 second, if so, prefer
            # the person exiting to the person entering
            if last_used < 0 or current[0] - last_used > 1:
                # print("The turnstile has not been used recently")
                # Let which ever one is exiting go first
                if current[1] == EXITING:
                    # print("Current person is exiting")
                    let_person_go(current, next_person, the_queue, return_times)
                    last_used = current[0]
                    last_direction = EXITING
                elif next_person[1] == EXITING:
                    # print("The next person is exiting")
                    let_person_go(next_person, current, the_queue, return_times)
                    last_used = next_person[0]
                    last_direction = EXITING
                # Looks like neither person is exiting, let current go
                else:
                    # print("Neither person is exiting")
                    let_person_go(current, next_person, the_queue, return_times)
                    last_used = current[0]
                    last_direction = current[1]
            # OK, so the turnstile has been recently used
            else:
                # They are both going the same direction, let current go
                # print("The turnstile has been used recently, last direction=%s" % ENETERING_EXITING[last_direction])
                # print("The current person: %s next person: %s" % (current, next_person))
                if current[1] == last_direction:
                    let_person_go(current, next_person, the_queue, return_times)
                    last_used = current[0]
                elif next_person[1] == last_direction:
                    let_person_go(next_person, current, the_queue, return_times)
                    last_used = next_person[0]
                # Change of direction, let the first person go
                else:
                    let_person_go(current, next_person, the_queue, return_times)
                    last_used = current[0]
                    last_direction = current[1]
        else:
            if current[0] == last_used:
                return_times[current[2]] = current[0] + 1
            else:
                return_times[current[2]] = current[0]
            last_direction = current[1]
            last_used = current[0]
    return return_times


if __name__ == '__main__':
    for i,input_data in enumerate(EXAMPLE_INPUTS):
        results = turnstile(times=input_data[0], directions=input_data[1])
        print("The results were: %s the expected results are: %s" % (results,
                                                                     EXPECTED_RESULTS[i]))
        print("     Times: %s" % input_data[0])
        print("Directions: %s" % input_data[1])
        print("%s" % ("="*80))
