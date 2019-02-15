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
