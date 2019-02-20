"""
# ******************************************************************************

#  Purpose        : To convert the temperature into celsius to fahrenheit
#
#  @file          : temperature_conversion.py
#  @author        : vishnu <vishnu840ranjan@gmail.com>
#  @version       : python 3.5
#  @since         : 18/02/2019

# ******************************************************************************
"""
from Utility.utility_algorithms import UtiltityAlgorithms

util = UtiltityAlgorithms()


class TemperatureConversion:
    try:
        result = util.temperature_conversion()  # calling the static method for temperature conversion
        print("Temperature = ", result)
    except Exception as error:
        print(repr(error))
