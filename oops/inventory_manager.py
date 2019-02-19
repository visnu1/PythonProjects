from Utility.utility_oops import Oops
import json
import traceback


class InventoryManager:
    try:

        inventory = Oops()  # Initialising the Oops object
        path = input(
            "Enter the file path: ")  # /home/bridgeit/pythonProjects/oops/json and text files/inventoryManager.json
        with open(path) as json_data:  # opening the json file
            data = json.load(json_data)  # reading the json data as strings
        data = inventory.inventory_calculations(data)  # calling the method for the inventory calculations
        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)  # writing the the data into the file

    except Exception as error:  # catching the error
        print(repr(error))
        traceback.print_stack()  # prints the error caught in the particular stack
