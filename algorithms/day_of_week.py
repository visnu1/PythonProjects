"""
# ******************************************************************************

#  Purpose        : To get the day of a week by accepting the date
#
#  @file          : day_of_week.py
#  @author        : vishnu <vishnu840ranjan@gmail.com>
#  @version       : python 3.5
#  @since         : 19/02/2019

# ******************************************************************************
"""
from Utility.utility_algorithms import UtiltityAlgorithms

import sys

util = UtiltityAlgorithms


class DayOfWeek:

    try:
        # To accept command line arguments
        day = int(sys.argv[1])  # 18
        month = int(sys.argv[2])  # 02
        year = int(sys.argv[3])  # 2019
        day_of_week = util.day_of_week(day, month, year)
        print(day_of_week)
    except Exception as err:
        print(repr(err))  # To represent the error
