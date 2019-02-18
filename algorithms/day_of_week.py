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
