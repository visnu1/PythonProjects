"""
# ******************************************************************************

#  Purpose        : To implement a 2D Array and accept the inputs from
#                   the user and print the result in the console
#  @file          : two_d_array.py
#  @author        : vishnu <vishnu840ranjan@gmail.com>
#  @version       : python 3.5
#  @since         : 24/01/2019

# ******************************************************************************
"""
from Utility.utility_functional import Utility, RowColumnError

util = Utility()


class TwoDarray:
    try:
        row = int(input("Enter the number of rows: "))
        column = int(input("Enter the number of columns: "))
        util.two_d_array(row, column)
    except RowColumnError as error:
        print(repr(error))
