from Utility.utility_functional import Utility

util = Utility()


class StopWatch:
    try:
        util.stopwatch()
    except Exception as err:
        print(repr(err))
        print("Error occurred sorry can't help")
