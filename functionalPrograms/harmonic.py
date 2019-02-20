"""
# ******************************************************************************

#  Purpose        : To get the harmonic number by accepting the number from the user
#  @file          : harmonic.py
#  @overview      : To get the nth harmonic number
#  @author        : vishnu <vishnu840ranjan@gmail.com>
#  @version       : python 3.6
#  @since         : 24/01/2019

# ******************************************************************************
"""
from Utility.utility_functional import Utility

util = Utility()


class Harmonic:
    try:
        number = int(input("Enter number to find the harmonic of the number: "))
        while number > 0:
            number = int(input("No negative integers: "))
        util.harmonic_number(number)
    except Exception as error:
        print(repr(error))
