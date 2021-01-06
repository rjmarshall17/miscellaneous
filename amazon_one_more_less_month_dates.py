#!/usr/bin/env python3

from datetime import datetime

START_DATE = 19700101
FIRST_LEAP_YEAR = 1972
NORMAL_DAYS = 365
LEAP_YEAR_DAYS = 366
MONTH_DAYS = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


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


def get_days_since_1970(year_in):
    total_days = 0
    for y in range(1970, year_in):
        if is_leap_year(y):
            total_days += LEAP_YEAR_DAYS
        else:
            total_days += NORMAL_DAYS
    return total_days


def get_days_in_year(get_year, get_month, get_day):
    days_in_year = 0
    for m in range(1, get_month):
        if m == 2 and is_leap_year(get_year):
            days_in_year += 29
        else:
            days_in_year += MONTH_DAYS[m]
    return days_in_year + get_day


EXAMPLE_INPUTS = [
    "20201125",
    "20050613",
]

if __name__ == '__main__':
    for i, input_data in enumerate(EXAMPLE_INPUTS):
        # The epoch date needs to be 12/31/1969 since 1/1/1970 is already 1 day.
        datetime_days = (datetime.strptime(input_data, '%Y%m%d') - datetime.strptime('19691231', '%Y%m%d')).days
        year = int(input_data[:4])
        month = int(input_data[4:6])
        day = int(input_data[6:])
        my_days = get_days_since_1970(year) + get_days_in_year(year, month, day)
        print("My days: %d datetime days: %d" % (my_days, datetime_days))
