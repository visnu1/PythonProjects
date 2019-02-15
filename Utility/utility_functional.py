import math
import random


class Utility:

    @staticmethod
    def string_replace(name):

        # To perform name validation
        if len(name) < 4 or name.isdigit():
            raise ValueError("Dear, person provide a proper name")  # raise Exception
        else:
            line = "Hello <<username>>, How are you?"
            line = line.replace("<<username>>", name)  # replacing the string with user name
            return line  # returning the string

    @staticmethod
    def flip_coin(number):

        tails, heads = 0, 0  # initialising the variables to keep count of the heads and tails
        if number > 1:
            for times in range(number):  # To flip the coin with the desired number of times
                if 0.5 > round(random.random(), 1):
                    heads += 1  # To increment heads
                else:
                    tails += 1  # To increment tails
        else:
            raise ValueError("Input arguments")  # raise exception

        print("Heads:" + str(heads) + "\nTails:" + str(tails))
        print("Number of times:" + str(number))
        # To print the percentage of heads and tails
        print("Heads:" + str((heads / number) * 100) + "%")
        print("Tails:" + str((tails / number) * 100) + "%")

    @staticmethod
    def leap_year(year):
        # if it divides with remainder zero then check weather it divides with 100
        if year % 4 == 0:
            # if it divides with remainder zero then check weather it divides with 400
            if year % 100 == 0:
                # check if it divides with 400 then return true
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    @staticmethod
    def power_of_2(number):

        if number < 31:
            n = 0
            print("Table: power of 2")
            while n < number:
                print("2^" + str(n) + " = " + str(pow(2, n)))
                n += 1
        else:
            raise ValueError("number should be in the range ( < 31)")

    @staticmethod
    def harmonic_number(number):
        sumo = 0
        if number > 0:
            for i in range(1, number, 1):  # starts form 1 , up to n and increment by 1
                sumo += 1 / i
                rounded_sum = round(sumo, 2)
                print("H" + str(i) + " = " + str(rounded_sum))
        else:
            raise ValueError("Illegal arguments")

    # @staticmethod
    # def stopwatch():

