
class Oops:

    @staticmethod
    def inventory_calculations(data):
        rice_prices = []
        wheat_prices = []
        pulses_prices = []
        for i, j, k in zip(data["rice"], data["wheat"], data["pulses"]):
            rice_prices.append(str(i['name']) + " = " + str(i['price'] * i['weight']))
            wheat_prices.append(str(j['name']) + " = " + str(j['price'] * j['weight']))
            pulses_prices.append(str(k['name']) + " = " + str(k['price'] * k['weight']))
        data = {}
        data['Total groceries value'] = []
        data['Total groceries value'].append({
            "rice price":rice_prices,
            "wheat price":wheat_prices,
            "pulses_prices":pulses_prices
        })
        return data
