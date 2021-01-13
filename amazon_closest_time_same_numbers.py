#!/usr/bin/env python3

"""
Given a time, e.g. 19:36, find the closest time using the same set of numbers without going more than
24 hours in advance.
"""


def get_valid_times(time_string):
    hours, minutes = time_string.split(':')
    numbers = set([x for x in hours + minutes])
    available_hours = set()
    available_minutes = set()
    for time_value in [i + j for i in numbers for j in numbers]:
        if int(time_value) < 24:
            available_hours.add(time_value)
        if int(time_value) <= 59:
            available_minutes.add(time_value)
    possible_times = {}
    start_time_value = int(hours) * 60 + int(minutes)
    for possible_hour in available_hours:
        for possible_minutes in available_minutes:
            if '%s:%s' % (possible_hour, possible_minutes) == time_string:
                continue
            minutes_to_check = int(possible_hour) * 60 + int(possible_minutes)
            minutes_plus_24 = (int(possible_hour) + 24) * 60 + int(possible_minutes)
            minutes_to_add = minutes_to_check if minutes_to_check > start_time_value else minutes_plus_24
            possible_times[minutes_to_add] = '%s:%s' % (possible_hour, possible_minutes)

    closest = None
    for check_time in possible_times.keys():
        if closest is None:
            closest = check_time
        # print("Checking time: %d (%d - %d = %d) - %s" % (check_time,
        #                                                  check_time,
        #                                                  start_time_value,
        #                                                  abs(check_time - start_time_value),
        #                                                  possible_times[check_time]))
        if abs(check_time - start_time_value) < abs(closest - start_time_value):
            # print("Setting closest to: %d - %s" % (check_time, possible_times[check_time]))
            closest = check_time
    return possible_times[closest]


EXAMPLE_INPUTS = [
    '19:36',
    '23:59',
    '11:49',
    '20:13',
]

EXPECTED_RESULTS = [
    '19:39',
    '22:22',
    '14:11',
    '20:20',
]

if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUTS):
        result = get_valid_times(input_data)
        output = "The result (%s) {0} the expected result (%s) for: %s" % (result,
                                                                           EXPECTED_RESULTS[i],
                                                                           input_data)
        assert result == EXPECTED_RESULTS[i], output.format('does not match')

        print(output.format('matches'))
