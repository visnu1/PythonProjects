"""
# ******************************************************************************

#  Purpose        : To determine the if the given year is leap year
#  @file          : leap_year.py
#  @author        : vishnu <vishnu840ranjan@gmail.com>
#  @version       : python 3.5
#  @since         : 24/01/2019

# ******************************************************************************
"""
from Utility.utility_functional import Utility

util = Utility()


class LeapYear:
    try:
        year = int(input("Enter the year:"))
        # loop over until a proper value is given
        while year < 999 or year > 9999:
            year = int(input("provide a proper year:"))
        if util.leap_year(year):  # check if it is a leap year by calling the static method
            print(str(year) + " is a leap year")

        else:
            print(str(year) + " is not a leap year")
    except Exception as error:
        print(repr(error))  # catch exceptions
