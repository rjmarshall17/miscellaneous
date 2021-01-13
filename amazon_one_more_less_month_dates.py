#!/usr/bin/env python3

from datetime import datetime

"""
Amazon Phone Interview Question January 5, 2021
Given two dates, determine if the dates are less than one month apart, exactly one month apart, or 
more than one month apart.
"""

NON_LEAP_YEAR_MONTH_DAYS = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LEAP_YEAR_MONTH_DAYS = [-1, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

DATE_INDICES = {
    'year':0,
    'month':1,
    'day':2,
}

DATE_FORMAT_INDICES = [
    (0,4),          # year
    (4,6),          # month
    (6,),           # day
]


def is_leap_year(check_year):
    if check_year % 4 == 0:
        if check_year % 100 == 0:
            if check_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    return False


def leap_years_since_year_1(year):
    if not isinstance(year, int):
        raise ValueError("The year must be an integer")
    if year < 1:
        raise ValueError("The year must be a positive integer")
    year -= 1
    return (year // 4) - (year // 100) + (year // 400)


def get_days_since_year_1(year):
	leap_years = leap_years_since_year_1(year)
	return (((year - 1) - leap_years) * sum(NON_LEAP_YEAR_MONTH_DAYS[1:]) + (leap_years * sum(LEAP_YEAR_MONTH_DAYS[1:])))


def get_days_since_1970(year_in):
    total_days = 0
    for y in range(1970, year_in):
        if is_leap_year(y):
            total_days += sum(LEAP_YEAR_MONTH_DAYS[1:])
        else:
            total_days += sum(NON_LEAP_YEAR_MONTH_DAYS[1:])
    return total_days


def get_days_in_year(get_year, get_month, get_day):
    days_in_year = 0
    for m in range(1, get_month):
        if m == 2 and is_leap_year(get_year):
            days_in_year += 29
        else:
            days_in_year += NON_LEAP_YEAR_MONTH_DAYS[m]
    return days_in_year + get_day


def are_dates_month_apart(date1: str, date2: str, use_year_1: bool) -> str:
    dates_by_days = {}
    for datestr in (date1, date2):
        # The date values will be year, month and day
        date_values = [-1] * 3
        for index in range(len(DATE_FORMAT_INDICES)):
            if len(DATE_FORMAT_INDICES[index]) > 1:
                date_values[index] = int(datestr[DATE_FORMAT_INDICES[index][0]:DATE_FORMAT_INDICES[index][1]])
            else:
                date_values[index] = int(datestr[DATE_FORMAT_INDICES[index][0]:])
        if use_year_1:
            dates_by_days[get_days_since_year_1(date_values[DATE_INDICES['year']]) +
                          get_days_in_year(date_values[DATE_INDICES['year']],
                                           date_values[DATE_INDICES['month']],
                                           date_values[DATE_INDICES['day']])] = date_values.copy()
        else:
            dates_by_days[get_days_since_1970(date_values[DATE_INDICES['year']]) +
                          get_days_in_year(date_values[DATE_INDICES['year']],
                                           date_values[DATE_INDICES['month']],
                                           date_values[DATE_INDICES['day']])] = date_values.copy()

    # We only have two dates, so check to see how far apart they are
    difference_in_days = abs(list(dates_by_days.keys())[0] - list(dates_by_days.keys())[1])
    # print("For %s and %s the difference is days is: %d" % (date1, date2, difference_in_days))
    min_date = min(list(dates_by_days.keys()))
    if is_leap_year(dates_by_days[min_date][0]):
        days_in_month = LEAP_YEAR_MONTH_DAYS[dates_by_days[min_date][1]]
    else:
        days_in_month = NON_LEAP_YEAR_MONTH_DAYS[dates_by_days[min_date][1]]
    if difference_in_days < days_in_month:
        return 'less than'
    elif difference_in_days > days_in_month:
        return 'greater than'
    else:
        return 'equal'


EXAMPLE_INPUTS = [
    ['20201125', '20201225'],
    ['20050613', '20060315'],
    ['19800504', '19800601'],
    ['20010101', '20010201'],
    ['20000215', '20000315'],
    ['20000215', '20000314'],
    ['20031215', '20040115'],
    ['19751223', '19760125'],
]

EXPECTED_RESULTS = [
    'equal',
    'greater than',
    'less than',
    'equal',
    'equal',
    'less than',
    'equal',
    'greater than',
]

if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUTS):
        # The epoch date needs to be 12/31/1969 since 1/1/1970 is already 1 day.
        # datetime_days = (datetime.strptime(input_data, '%Y%m%d') - datetime.strptime('19691231', '%Y%m%d')).days
        result = are_dates_month_apart(input_data[0], input_data[1], False)
        result2 = are_dates_month_apart(input_data[0], input_data[1], True)
        assert result == result2, "1970 and year one differ: %s != %s" % (result, result2)
        assert result == EXPECTED_RESULTS[i], \
            "For %s and %s the result (%s) does not match the expected result: %s" % (input_data[0],
                                                                                      input_data[1],
                                                                                      result,
                                                                                      EXPECTED_RESULTS[i])
        print("The result was as expected for %s and %s: %s" % (input_data[0],
                                                                input_data[1],
                                                                result))
