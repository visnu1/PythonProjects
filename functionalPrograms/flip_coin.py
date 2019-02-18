# ******************************************************************************

#  Purpose        : The no of times the coin to be flipped is provided by the user
#                   and percentage of appearance of  heads and tails are to be determined
#  @file          : flip_coin.py
#  @overview      : To determine the percentage of Heads & Tails
#  @author        : vishnu <vishnu840ranjan@gmail.com>
#  @version       : python 3.5
#  @since         : 24/01/2019

# ******************************************************************************

""" hello """
from Utility.utility_functional import Utility

util = Utility()


class FlipCoin:
    try:
        number = int(input("Enter the number of times the coin to be flipped: "))
        while number < 1:
            input("Enter a proper valid number: ")
        util.flip_coin(number)
    except Exception as error:
        print(repr(error))
