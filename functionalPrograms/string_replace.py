"""
# ******************************************************************************

#  Purpose        : To replace the string using the given string
#
#  @file          : stopwatch.py
#  @author        : vishnu <vishnu840ranjan@gmail.com>
#  @version       : python 3.5
#  @since         : 24/01/2019

# ******************************************************************************
"""
from Utility.utility_functional import Utility

# Initialisation of utility class
util = Utility()


class StringReplace:

    try:
        print(util.string_replace(input("Enter your name: ")))  # Taking user inputs and printing
    except Exception as errorName:  # handling Exception
        print("Error occurred:" + repr(errorName))
