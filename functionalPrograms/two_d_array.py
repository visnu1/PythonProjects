from Utility.utility_functional import Utility, RowColumnError

util = Utility()


class TwoDarray:
    try:
        row = int(input("Enter the number of rows: "))
        column = int(input("Enter the number of columns: "))
        util.two_d_array(row, column)
    except RowColumnError as error:
        print(repr(error))
