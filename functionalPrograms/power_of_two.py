from Utility.utility_functional import Utility

util = Utility()


class PowerOfTwo:
    try:
        number = int(input("Enter a number to find all the power of 2: "))
        while number > 31:
            number = int(input("Enter the number in the range 0 - 31"))
        util.power_of_2(number)
    except Exception as error:
        print(repr(error))  # catch exception and print the exception string
