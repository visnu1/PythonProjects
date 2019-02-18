from Utility.utility_algorithms import UtiltityAlgorithms

import traceback

util = UtiltityAlgorithms()


class PrimeNumbers:
    try:
        range1 = int(input("Enter the initial range = "))
        range2 = int(input("Enter the end range = "))
        result = util.prime_numbers(range1, range2)
        print("Prime numbers in the range ", range1, "-", range2, " are: ", result)
    except Exception as error:
        print(repr(error))
        traceback.print_exc()
