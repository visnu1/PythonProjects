class Address:

    def __init__(self, state, city, zip_code, phone):
        self.__state = state
        self.__city = city
        self.__zip = zip_code
        self.__phone = phone

    def set_state(self, state):
        self.__state = state

    def set_city(self, city):
        self.__city = city

    def set_zip(self, zip_code):
        self.__zip(int(zip_code))

    def set_phone(self, phone):
        self.__phone(int(phone))

    def get_state(self):
        return self.__state

    def get_city(self):
        return self.__city

    def get_zip(self):
        return self.__zip

    def get_phone(self):
        return self.__phone
