#!/usr/bin/env python3

from typing import List

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


def add_up_all_movies(first_index, movie_duration, all_movie_duration):
    if first_index >= len(movie_duration):
        return all_movie_duration
    for second_index in range(first_index+1,len(movie_duration)):
        all_movie_duration.append((movie_duration[first_index] + movie_duration[second_index],
                                   movie_duration[first_index],
                                   movie_duration[second_index]))
    add_up_all_movies(first_index+1, movie_duration, all_movie_duration)


if __name__ == '__main__':
    all_movie_duration = []
    all_durations = add_up_all_movies(0, movie_duration, all_movie_duration)
    previous = None
    for movie_times in sorted(all_movie_duration, key=lambda x: x[0]):
        if movie_times[0] > flight_duration - 30:
            print("The best movies are: %d, %d = %d" % (previous[1], previous[2], previous[0]))
            break
        previous = movie_times
