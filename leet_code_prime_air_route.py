#!/usr/bin/env python3
from pprint import pprint

"""
Amazon Prime Air is developing a system that divides shipping routes using
flight optimization routing systems to a cluster of aircraft that can 
fulfill these routes. Each shipping route is identified by a unique integer
identifier, requires a fixed non-zero amount of travel distance between
airports, and is defined to be either a forward shipping route or a return
shipping rout. Identifiers are guaranteed to be unique within their own
route type, but not across route types.

Each aircraft should be assigned two shipping routes at once: one forward
route and one return route. Due to the complex scheduling of flight plans, 
all aircraft have a fixed maximum operating travel distance, and cannot
be scheduled to fly a shipping route that requires more travel distance
than the prescribed maximum opeerating travel distance. The goal of the
system is to optimize the total operating travel distance of a given aircraft.
A forward/return shipping rout pair is considered to be "optimal" if there 
does not exist another pair that has a higher operating travel travel distance
than this pair, and also has a total less than or equal to the maximum 
operating travel distance of the aircraft.

For example, if the aircraft has a maximum operating travel distance of 3,000
miles, a forward/return shipping route pair using a total of 2,900 miles would
be optimal if there does not exist a pair that uses a total operating travel
distance of 3,000 miles, but would not be considered optimal if such a 
pair did exist.

Your task is to write an algorithm to optimize the sets of forward/return
shipping route pairs that allow the aircraft to be optimally utilized, given
a list of forward shipping routes and a list of return shipping routes.

Input:

The input to the function/method consists of three arguments:

- maxTravelDist, an integer representing the maximum operating travel distance
  of a given aircraft;
- forwardRouteList, a list of pairs of integers where the first integer
  represents the unique identifier of a forward shipping route and the second
  integer represents the amount of travel distance required by this shipping
  route;
- returnRouteList, a list of pairs of integers where the first integer represents
  the unique identifier of a return shipping route and the second integer
  represents the amount of travel distance required by this shipping route.

Output:

Return a list of pairs of integers representing the pairs of IDs of forward and
return shipping routes that optimally utilize the given aircraft. If no route
is possible, return a list with an empty pair.

Examples:

Input:
    maxTravelDist = 7000
    forwardRouteList = [[1,2000],[2,4000],[3,6000]]
    returnRouteList = [[1,2000]]

Output:
    [[2,1]]

Explanation:

There are only three combinations: [1,1], [2,1], and [3,1], which have a total of
4,000, 6,000 and 8,000 miles respectively. Since 6,000 is the largest use that does
not exceed 7,000 [2,1] is the only optimal pair.

"""

EXAMPLE_INPUT = [
    (11, [[1, 5], [2, 5]], [[1, 5], [2, 5]]),
    (10, [[1, 5], [2, 5]], [[1, 5], [2, 5]]),
    (20, [[1, 8], [2, 7], [3, 14]], [[1, 5], [2, 10], [3, 14]]),
    (20, [[1, 8], [2, 15], [3, 9]], [[1, 8], [2, 11], [3, 12]]),
    (7000, [[1, 2000], [2, 4000], [3, 6000]], [[1, 2000]]),
]

EXPECTED_RESULTS = [
    [[1, 1], [1, 2], [2, 1], [2, 2]],
    [[1, 1], [1, 2], [2, 1], [2, 2]],
    [[3, 1]],
    [[1, 3], [3, 2]],
    [[2, 1]],
]


def optimal_flight_path(max_travel_distance, forward_route_list, return_route_list):
    # If we don't have either a forward_route_list and/or a return_route_list, return
    # an empty list. Check for a constraint the may make this test unnecessary.
    if not forward_route_list or not return_route_list:
        return []

    # If we have an invalid max_travel_distance - check for a constraint on
    # this to see if this check is necessary.
    if max_travel_distance <= 0:
        return []

    # Combine all of the incoming forward and return routes in the maximum number
    # of combinations and loop through them.
    # Looping through the incoming forward and return route lists has a time complexity
    # of O(n+m) where n is the length of the forward route list and m is the length of
    # the return route list. The space complexity is O(1) for the for expression.
    best_distance = []

    # The format of the incoming forward and return route lists is: [ID, distance]
    for distance, to_from_route in [[frl[1] + rrl[1], [frl[0], rrl[0]]] for frl in forward_route_list
                                    for rrl in return_route_list]:
        # Inserts into the best_distance list are: time: O(1). But depending on the distances,
        # there may be more than one, so the worst case here is O(x) where x is the number of
        # distances that are less than or equal to the max_travel_distance, space: O(n)
        if distance <= max_travel_distance:
            if best_distance:
                if distance == best_distance[0]:
                    best_distance[1].append(to_from_route)
                elif distance > best_distance[0]:
                    best_distance = [distance, [to_from_route]]
            else:
                best_distance = [distance, [to_from_route]]

    # The time complexity for this function is: O(n+m) (see above)
    return best_distance[1]


if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUT):
        results = optimal_flight_path(input_data[0], input_data[1], input_data[2])
        assert results == EXPECTED_RESULTS[i]
        print("The results for input %d matched the expected results: %s" % (i,results))
