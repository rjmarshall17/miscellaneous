#!/usr/bin/env python3

from typing import List
from itertools import combinations


"""
You are on a flight and want to watch two movies during the flight. You are
given int[] movie_duration which includes all movie durations.

You are also given the duration of the flight which is d minutes. Pick two 
movies where the total duration is less than or equal to d - 30 minutes.

Find the pair of movies with the longest total duration. If multiple found,
return the pair with the longest movie.
"""

movie_duration = [90, 85, 75, 60, 120, 150, 125]
flight_duration = 250


# The time complexity for both of these, either iterative or recursive, is O(n**2)
# Instead of nested for loops we could use the itertools combinations function, but
# my assumption here is that it will still take the same amount of effort for that
# to come up with all of the combinations. I tested with timeit for both functions,
# i.e. the one that manually stepped through the combinations and using the itertools
# combinations. The itertools combinations was slightly, 6.5 vs 5.5, faster. So, for
# now I'm leaving this as the original nested for loops.
def add_up_all_movies_iterative(movie_durations_in):
    ret = set()
    for index in range(0,len(movie_durations_in)):
        for index2 in range(index + 1, len(movie_durations_in)):
            ret.add((movie_durations_in[index] + movie_durations_in[index2],
                     movie_durations_in[index],
                     movie_durations_in[index2]))
    return list(ret)


def add_up_all_movies_recursive(first_index, movie_duration_in, all_movies_durations_in):
    if first_index >= len(movie_duration_in):
        return all_movies_durations_in
    for second_index in range(first_index+1, len(movie_duration_in)):
        all_movies_durations_in.append((movie_duration_in[first_index] + movie_duration_in[second_index],
                                        movie_duration_in[first_index],
                                        movie_duration_in[second_index]))
    add_up_all_movies_recursive(first_index+1, movie_duration_in, all_movies_durations_in)


if __name__ == '__main__':
    all_movies_durations = []
    add_up_all_movies_recursive(0, movie_duration, all_movies_durations)
    iterative_all_movies_durations = add_up_all_movies_iterative(movie_duration)
    assert sorted(all_movies_durations) == sorted(iterative_all_movies_durations)
    print("Length of original list: %d length of all durations: %d" % (len(movie_duration),
                                                                       len(all_movies_durations)))
    previous = None
    for movie_times in sorted(all_movies_durations, key=lambda x: x[0]):
        if movie_times[0] > flight_duration - 30:
            print("The best movies are: %d, %d = %d" % (previous[1], previous[2], previous[0]))
            break
        previous = movie_times
