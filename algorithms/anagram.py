from Utility.utility_algorithms import UtiltityAlgorithms

util = UtiltityAlgorithms()


class Anagram:
    try:

        # To check if the given two strings are equal by accepting two strings and calling the function
        if util.check_anagram(input("Enter the first element:"), input("Enter the second element:")):
            print("The given two strings are anagram")  #
        else:
            print("The two strings are not anagram")
    except Exception as error:
        print(repr(error))
