"""
# ******************************************************************************

#  Purpose        : To read elements from a file and perform
#                   insert or delete the element depending on the availability using linked list
#  @file          : unordered.py
#  @author        : vishnu <vishnu840ranjan@gmail.com>
#  @version       : python 3.5
#  @since         : 16/02/2019

# ******************************************************************************
"""
from Utility.utility_datastructures import LinkedList


class Unordered:
    try:

        path = input(
            "Enter the file path/file name: ")  # /home/bridgeit/pythonProjects/DataStructures/Text Files/readable.txt
        file = open(path, "r")  # opens the file for the given path
        data = file.read()  # reads the data in the file
        list = data.split(" ")  # splits the data by whitespace
        linked_list = LinkedList()  # instantiating linked_list object
        for x in list:  # looping over and adding the data into the linked list
            linked_list.add(x)
        element = input("Enter the string to be searched = ")
        if linked_list.search(element):  # search for the string in the linked_list
            while linked_list.search(element):
                linked_list.remove(element)  # if the element is found remove
        else:
            linked_list.add(element)  # if the element is not found add the element

        list = linked_list.print()
        data = ""
        for x in list:
            data = data + str(x) + " "  # To concatenate all the elements
        print(data)
        file = open(path, 'w')
        file.write(data)  # to write the data into the file

    except Exception as err:
        print(repr(err))
    finally:
        file.close()
