"""
# ******************************************************************************

#  Purpose        : To implement a stopwatch
#
#  @file          : stopwatch.py
#  @author        : vishnu <vishnu840ranjan@gmail.com>
#  @version       : python 3.5
#  @since         : 24/01/2019

# ******************************************************************************
"""
from Utility.utility_functional import Utility

util = Utility()


class StopWatch:
    try:
        util.stopwatch()
    except Exception as err:
        print(repr(err))
        print("Error occurred sorry can't help")
