#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date utilities for the Scotland Trip Planner.

This module provides functions for date and time handling,
including date ranges, weekends, and holidays.
"""

import datetime
from typing import List, Tuple

# UK bank holidays for 2023 (update as needed)
UK_HOLIDAYS_2023 = [
    datetime.date(2023, 1, 2),   # New Year's Day (substitute)
    datetime.date(2023, 1, 3),   # New Year's Holiday (Scotland)
    datetime.date(2023, 4, 7),   # Good Friday
    datetime.date(2023, 4, 10),  # Easter Monday
    datetime.date(2023, 5, 1),   # Early May Bank Holiday
    datetime.date(2023, 5, 29),  # Spring Bank Holiday
    datetime.date(2023, 8, 7),   # Summer Bank Holiday (Scotland)
    datetime.date(2023, 11, 30), # St Andrew's Day (Scotland)
    datetime.date(2023, 12, 25), # Christmas Day
    datetime.date(2023, 12, 26), # Boxing Day
]

def is_weekend(date):
    """Check if a date is a weekend."""
    return date.weekday() >= 5  # 5 = Saturday, 6 = Sunday

def is_holiday(date, holidays=None):
    """Check if a date is a holiday."""
    if holidays is None:
        holidays = UK_HOLIDAYS_2023
    return date in holidays

def is_weekend_or_holiday(date, holidays=None):
    """Check if a date is a weekend or a holiday."""
    return is_weekend(date) or is_holiday(date, holidays)

def get_next_weekend(start_date=None):
    """Get the dates for the next weekend."""
    # TODO: Implement next weekend calculation
    pass

def get_date_range(start_date, end_date):
    """Get a list of dates in a range."""
    # TODO: Implement date range calculation
    pass

def format_date(date, format_str="%Y-%m-%d"):
    """Format a date as a string."""
    return date.strftime(format_str)

def parse_date(date_str, format_str="%Y-%m-%d"):
    """Parse a date string."""
    return datetime.datetime.strptime(date_str, format_str).date()