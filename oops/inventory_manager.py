import json


class InventoryManager:
    try:

        path = input(
            "Enter the file path: ")  # /home/bridgeit/pythonProjects/oops/json and text files/inventoryManager.json
        with open(path) as json_data:
            data = json.load(json_data)
        rice = data.rice
        wheat = data.wheat
        pulses = data.pulses
        total_price = 0
        arr = []
        for p in pulses:


    except Exception as error:
        print(repr(error))
