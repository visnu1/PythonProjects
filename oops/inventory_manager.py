from Utility.utility_oops import Oops
import json


class InventoryManager:
    try:

        inventory = Oops()
        path = input(
            "Enter the file path: ")  # /home/bridgeit/pythonProjects/oops/json and text files/inventoryManager.json
        with open(path) as json_data:
            data = json.load(json_data)
        data = inventory.inventory_calculations(data)
        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)

    except Exception as error:
        print(repr(error))
