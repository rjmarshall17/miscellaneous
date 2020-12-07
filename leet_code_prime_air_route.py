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
    (11, [[1, 5], [2, 5]], [ [1, 5], [2, 5] ]),
    (10, [[1, 5], [2, 5]], [ [1, 5], [2, 5] ]),
    (20, [[1, 8], [2, 7], [3, 14]], [[1, 5], [2, 10], [3, 14]]),
    (20, [[1, 8], [2, 15], [3, 9]], [[1, 8], [2, 11], [3, 12]]),
    (7000, [[1, 2000], [2, 4000], [3, 6000]], [[1, 2000]]),
]


def optimal_flight_path(max_travel_distance, forward_route_list, return_route_list):
    # Combine all of the incoming forward and return routes in the maximum number
    # of combinations. Add them to a "route table" which is a dictionary where the
    # key is the distance for that combination of routes.
    # print("The max travel distance is: %d" % max_travel_distance)
    route_table = {}

    # The initial creation of the route_table has a time complexity of: O(n+m) where
    # n is the length of the forward route list and m is the length of the return
    # route list. The space complexity is O(1) for the for expression since, at this
    # point I'm not putting the returned values anywhere, that comes later.
    for to_from_route in [[[x[0], y[0]], x[-1] + y[-1]] for x in forward_route_list for y in return_route_list]:
        # print("The total for routes %s is: %d" % (to_from_route[0], to_from_route[1]))
        # Inserts into a dictionary are time: O(1), space: O(n)
        if to_from_route[1] in route_table:
            route_table[to_from_route[1]].append(to_from_route[0])
        else:
            route_table[to_from_route[1]] = [to_from_route[0]]

    # print("The route table is:")
    # pprint(route_table)
    # print("The route table values are: %s" % list(route_table.values()))
    #
    # Time complexity for keys() for Python3 is O(1)
    if len(route_table.keys()) == 1:
        # Converting the route_table keys to a list is potentially
        # O(N) from a time complexity standpoint. And O(k), where k
        # is the number of keys, from a space complexity issue.
        # Since we appear to have only one distance for all of the
        # routes, and it's farther than max_travel_distance, we
        # return an empty list.
        if list(route_table.keys())[0] > max_travel_distance:
            print("Best route(s): %s" % [])
        else:
            # It appears that the only distance is less than or equal
            # to the max_travel_distance, so all routes would be the
            # most optimal we can get for this set of routes.
            print("Best route(s): %s" % list(route_table.values())[0])
    else:
        # We have more than one distance, let's find the one(s) that
        # come closest to the max_travel_distance, i.e. the best/most
        # optimal distance.
        best_distance = None
        # Looping through all of the items in the route_table dictionary
        # will have a time complexity of O(n).
        for distance, route in route_table.items():
            if distance <= max_travel_distance:
                # Let's see if the current route is a more optimal route than
                # the one we have so far.
                if best_distance:
                    if distance > best_distance[0]:
                        best_distance = [distance, route]
                else:
                    best_distance = [distance, route]
        print("Best route(s}: %s" % best_distance[1])
    print("="*80)

if __name__ == '__main__':
    for input_data in EXAMPLE_INPUT:
        optimal_flight_path(input_data[0], input_data[1], input_data[2])
