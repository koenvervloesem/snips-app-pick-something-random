#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains some utility functions used by the
'Pick something random' app.
"""

from calendar import monthrange
from datetime import date, timedelta
from random import randint


def string_to_date(date_string):
    """
    Return a date object from a date string in ISO 8601 format.
    """

    return date(int(date_string[:4]),
                int(date_string[5:7]),
                int(date_string[8:10]))


def random_date(from_date, to_date):
    """
    Return a random date object between two date objects.
    """

    return date.fromordinal(randint(from_date.toordinal(),
                                    to_date.toordinal()))


def get_period_from_grainy_time(time_value):
    """
    Return a tuple with the start date and end date of a grainy
    InstantTimeValue object.
    """

    if time_value.grain == 4:  # "Day"
        start_date = end_date = string_to_date(time_value.value)
    elif time_value.grain == 3:  # "Week"
        # Add 6 days to get the end of the week.
        start_date = string_to_date(time_value.value)
        end_date = start_date + timedelta(days=6)
    elif time_value.grain == 2:  # "Month"
        # Get the day of the end of the month.
        start_date = string_to_date(time_value.value)
        days_in_month = monthrange(start_date.year, start_date.month)[1]
        end_date = start_date.replace(day=days_in_month)
    # TODO: What is period.grain == 1?
    elif time_value.grain == 0:  # "Year"
        # Get the day of the end of the year.
        start_date = string_to_date(time_value.value)
        end_date = start_date.replace(month=12, day=31)

    return (start_date, end_date)
