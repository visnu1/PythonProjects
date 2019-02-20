from abc import ABCMeta, abstractmethod


# Interface
class AddressBook(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def operation(self): pass

    @abstractmethod
    def add(self): pass

    @abstractmethod
    def edit(self): pass

    @abstractmethod
    def delete(self): pass

    @abstractmethod
    def sort_by_name(self): pass

    @abstractmethod
    def sort_by_zip(self): pass
