import json


def get_capital(state):
    with open('database/country_capital.json') as json_file:
        data = json.load(json_file)
        for line in data:
            if state.lower() == line['country'].lower():
                return line['city']


def rename_country(code):
    with open('database/country_code.json') as json_file:
        data = json.load(json_file)
        for country in data:
            if country['code'] == code:
                return country['name']
    return code

def loc_list_to_human(loc_list):
    """[['Jerusalem', 'US', 'RI', 'Washington County', {'lat': 41.376701, 'lng': -71.518097}]]
    transform to [[Jerusalem,Washington County,RI,US ]]"""
    human_loc = []
    for loc in loc_list:
        append_string = ""
        append_order = [0, 3, 2, 1]
        if len(loc[1]) < 3:
            loc[1] = rename_country(loc[1])
        if len(loc[0]) < 2:
            loc[0] = get_capital(loc[1])
        for i in append_order:
            if len(loc[i]) > 0:
                append_string += (loc[i] + " ")
        human_loc.append(append_string)
    return human_loc

class weather:
    """Weather object:
    country : string
    city : string
    district: string
    max_temp : {0: int, 1: int, 2: int, 3: int, 4: int, 5: int , 6: int}
    min_temp : {0: int, 1: int, 2: int, 3: int, 4: int, 5: int , 6: int}
    humidity :  {0: int, 1: int, 2: int, 3: int, 4: int, 5: int , 6: int}"""
    def __init__(self, country, city, district, max_temp, min_temp, humidity, status):
        self.country = country
        self.district = district
        self.city = city
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.humidity = humidity
        self.status = status
