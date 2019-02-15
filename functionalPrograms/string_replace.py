from Utility.utility_functional import Utility

# Initialisation of utility class
util = Utility()


class StringReplace:

    try:
        print(util.string_replace(input("Enter your name: ")))  # Taking user inputs and printing
    except Exception as errorName:  # handling Exception
        print("Error occurred:" + repr(errorName))
