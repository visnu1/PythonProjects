import math


# Exception class object for invalid range
class RangeException(Exception):

    def __init__(self, arg):
        self.args = arg


# Exception class for illegal arguments
class IllegalArguments(Exception):
    def __init__(self, arg):
        self.args = arg


class UtiltityAlgorithms:

    @staticmethod
    def check_anagram(element1, element2):

        if len(element1) == len(element2):  # To check the length of the strings

            str1 = ""
            str2 = ""
            element1 = list(element1.lower())  # To convert the string into lowercase and to split by characters
            element2 = list(element2.lower())
            element1.sort()  # To sort the characters in the list
            element2.sort()
            for x in element1:
                str1 += x  # To concatenate the characters
            for x in element2:
                str2 += x

            if str1 == str2:  # To check if the two concatenated strings are equal
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def prime_numbers(range1, range2):

        # To perform input validation for the parameters
        if range1 > range2 or range1 < 0 or range2 < 0:
            raise RangeException("Provide a proper range")  # raising an exception for a proper range
        else:

            prime_array = []
            # Initialising the range for the variables
            low, high = range1, range2
            while low <= high:
                flag = False
                for i in range(2, int(low / 2)):
                    if low % i == 0:  # condition for non prime numbers
                        flag = True
                        break

                if not flag and low != 4:  # Enters the loop only for prime numbers

                    if low != 0:  # If it is a prime number, add it to the array
                        prime_array.append(low)
                low += 1
            return prime_array  # returns an array containing prime numbers

    @staticmethod
    def to_binary(number):

        if number > 0:
            # declaring the variables
            string = binary = ""
            arr = []
            n = 0
            while number > 0:  # loop until the given number is completely divided
                result = number % 2
                if result == 1:
                    binary = str(result) + binary  # all the binary digits are concatenated
                    string = str(math.pow(2, n) * 1) + " + " + str(
                        string)  # all the sum of powers of two are concatenated
                else:
                    binary = str(result) + binary  # all the binary digits are concatenated
                    string = '0' + " + " + str(string)
                n += 1
                number = int(math.floor(number / 2))  # To reduce the given number

            while len(binary) < 8:  # to concatenate zeros at the MSB bit i.e padding of zeros is done
                binary = "0" + str(binary)
            arr.append(binary)
            arr.append(string)
            return arr
        else:
            raise IllegalArguments("Arguments not of valid type")

    @staticmethod
    def day_of_week(date, month, year):

        if 999 < year and year < 10000 and 0 < month and month < 13 and 0 < date and date < 32:

            # formula to calculate the day of the week
            y0 = year - math.trunc((14 - month) / 12)
            x = y0 + math.trunc((y0 / 4)) - math.trunc((y0 / 100)) + math.trunc((y0 / 400))
            m0 = month + 12 * math.trunc((14 - month) / 12) - 2
            d0 = (date + x + math.trunc((31 * m0) / 12)) % 7
            # To switch for the case depending on the day obtained through calculations using dictionary
            day_name = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday",
                        6: "Saturday"}
            return day_name[d0]  # return the day of the week
        else:
            raise IllegalArguments("Provide a proper date")

    @staticmethod
    def temperature_conversion():

        # To ask weather the user wants it to be converted into celsius or Fahrenheit
        option = int(input("Enter\n1.To convert Celsius to Fahrenheit: \n2.To convert Fahrenheit to Celsius:\n"))
        while True:
            if option == 1 or option == 2:
                break
            option = int(input("Provide a proper choice: "))
        # To ask the user to input the temperature
        temperature = int(input("Enter the temperature: "))
        if option:  # To convert Celsius to Fahrenheit
            temperature = round((temperature * (9 / 5)) + 32)
            return str(temperature) + " F"
        else:  # To convert Fahrenheit to Celsius
            temperature = round((temperature - 32) * (5 / 9))
            return str(temperature) + " C"
