from Utility.utility_algorithms import UtiltityAlgorithms

util = UtiltityAlgorithms()


class TemperatureConversion:
    try:
        result = util.temperature_conversion()  # calling the static method for temperature conversion
        print("Temperature = ", result)
    except Exception as error:
        print(repr(error))
