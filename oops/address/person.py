class Person:

    def __init__(self, fname, lname, address):
        self.__first_name = fname
        self.__last_name = lname
        self.__address = address

    def set_first_name(self, name):
        self.__first_name = name

    def set_last_name(self, name):
        self.__last_name = name

    def set_address(self, address):
        self.__address = address

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address
