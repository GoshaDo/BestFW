import json
from datetime import date

def get_capital(state):
    """Function which return capital name of a state, if not found returns None"""
    with open('database/country_capital.json') as json_file:
        data = json.load(json_file)
        for line in data:
            if state.lower() == line['country'].lower():
                return line['city']


def rename_country(code):
    """Function which returns country name out of code of the country
    if not found returns the code"""
    with open('database/country_code.json') as json_file:
        data = json.load(json_file)
        for country in data:
            if country['code'] == code:
                return country['name']
    return code


def loc_list_to_human(loc_list):
    """Function which translate API's loc_list to humans"""
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


def is_valid_date(input):
    dd = input[:2]
    mm = input[3:5]
    yyyy = input[6:10]
    if len(yyyy) < 4:
        return False
    try:
        dd = int(dd)
        mm = int(mm)
        yyyy = int(yyyy)
    except ValueError:
        return False

    today = date.today()
    if not (0 <= dd <= 31 and 0 <= mm <= 12 and 2000 <= yyyy <= today.year):  # de-morgan
        return False

    return True


if __name__ == "__main__":
    print(is_valid_date("12/12/2021"))
