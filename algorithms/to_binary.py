"""
# ******************************************************************************

#  Purpose        : To convert the given decimal number into binary
#
#  @file          : to_binary.py
#  @author        : vishnu <vishnu840ranjan@gmail.com>
#  @version       : python 3.5
#  @since         : 17/02/2019

# ******************************************************************************
"""
import traceback

from Utility.utility_algorithms import UtiltityAlgorithms

util = UtiltityAlgorithms()


class ToBinary:
    try:
        number = int(input("Enter the number to be converted into binary = "))  # To accept a number
        array = util.to_binary(number)  # calling the function to return back the binary format of the given number
        print(number, " in binary = ", array[0])  # print the binary format of the number
        print("sum of power of two = ", array[1])
    except Exception as err:
        print(repr(err))  # to print the error message
        traceback.print_exc()  # To trace the error in a particular line
